"""
Direct Python API for workout_api package.
Allows programmatic access without HTTP calls.
"""
from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession

from workout_api.atleta.schemas import AtletaIn, AtletaOut
from workout_api.categorias.schemas import CategoriaIn, CategoriaOut
from workout_api.centro_treinamento.schemas import CentroTreinamentoIn, CentroTreinamentoOut
from workout_api.configs.database import async_session

# Import controller functions
from workout_api.categorias import controller as categoria_controller
from workout_api.centro_treinamento import controller as centro_controller
from workout_api.atleta import controller as atleta_controller


class BaseService:
    """Base service class with common session management."""
    
    def __init__(self, session: Optional[AsyncSession] = None):
        self._session = session
        self._should_close = False
    
    async def _get_session(self) -> AsyncSession:
        """Get or create database session."""
        if self._session is None:
            self._session = async_session()
            self._should_close = True
        return self._session
    
    async def _close_session(self):
        """Close session if it was created by this service."""
        if self._should_close and self._session:
            await self._session.close()
            self._session = None
            self._should_close = False


class CategoriaService(BaseService):
    """Service for Categoria operations."""
    
    async def create(self, nome: str) -> CategoriaOut:
        """Create a new categoria."""
        try:
            session = await self._get_session()
            categoria_in = CategoriaIn(nome=nome)
            result = await categoria_controller.post(db_session=session, categoria_in=categoria_in)
            return result
        finally:
            await self._close_session()
    
    async def get_all(self) -> List[CategoriaOut]:
        """Get all categorias."""
        try:
            session = await self._get_session()
            result = await categoria_controller.query(db_session=session)
            return result
        finally:
            await self._close_session()


class CentroTreinamentoService(BaseService):
    """Service for Centro de Treinamento operations."""
    
    async def create(
        self,
        nome: str,
        endereco: str,
        proprietario: str
    ) -> CentroTreinamentoOut:
        """Create a new centro de treinamento."""
        try:
            session = await self._get_session()
            centro_in = CentroTreinamentoIn(
                nome=nome,
                endereco=endereco,
                proprietario=proprietario
            )
            result = await centro_controller.post(
                db_session=session,
                centro_treinamento_in=centro_in
            )
            return result
        finally:
            await self._close_session()
    
    async def get_all(self) -> List[CentroTreinamentoOut]:
        """Get all centros de treinamento."""
        try:
            session = await self._get_session()
            result = await centro_controller.query(db_session=session)
            return result
        finally:
            await self._close_session()


class AtletaService(BaseService):
    """Service for Atleta operations."""
    
    async def create(
        self,
        nome: str,
        cpf: str,
        idade: int,
        peso: float,
        altura: float,
        sexo: str,
        categoria_nome: str,
        centro_treinamento_nome: str
    ) -> AtletaOut:
        """Create a new atleta."""
        try:
            session = await self._get_session()
            atleta_in = AtletaIn(
                nome=nome,
                cpf=cpf,
                idade=idade,
                peso=peso,
                altura=altura,
                sexo=sexo,
                categoria=CategoriaIn(nome=categoria_nome),
                centro_treinamento=CentroTreinamentoIn(
                    nome=centro_treinamento_nome,
                    endereco="",
                    proprietario=""
                )
            )
            result = await atleta_controller.post(db_session=session, atleta_in=atleta_in)
            return result
        finally:
            await self._close_session()
    
    async def get_all(self, nome: Optional[str] = None) -> List[AtletaOut]:
        """Get all atletas, optionally filtered by name."""
        try:
            session = await self._get_session()
            result = await atleta_controller.query(db_session=session, nome=nome)
            return result
        finally:
            await self._close_session()


# ==================== BACKWARD COMPATIBILITY ====================
# Keep functional API for backward compatibility

async def create_categoria(nome: str, session: Optional[AsyncSession] = None) -> CategoriaOut:
    """Create a new categoria programmatically."""
    service = CategoriaService(session)
    return await service.create(nome)


async def get_all_categorias(session: Optional[AsyncSession] = None) -> List[CategoriaOut]:
    """Get all categorias."""
    service = CategoriaService(session)
    return await service.get_all()


async def create_centro_treinamento(
    nome: str,
    endereco: str,
    proprietario: str,
    session: Optional[AsyncSession] = None
) -> CentroTreinamentoOut:
    """Create a new centro de treinamento programmatically."""
    service = CentroTreinamentoService(session)
    return await service.create(nome, endereco, proprietario)


async def get_all_centros_treinamento(session: Optional[AsyncSession] = None) -> List[CentroTreinamentoOut]:
    """Get all centros de treinamento."""
    service = CentroTreinamentoService(session)
    return await service.get_all()


async def create_atleta(
    nome: str,
    cpf: str,
    idade: int,
    peso: float,
    altura: float,
    sexo: str,
    categoria_nome: str,
    centro_treinamento_nome: str,
    session: Optional[AsyncSession] = None
) -> AtletaOut:
    """Create a new atleta programmatically."""
    service = AtletaService(session)
    return await service.create(nome, cpf, idade, peso, altura, sexo, categoria_nome, centro_treinamento_nome)


async def get_all_atletas(session: Optional[AsyncSession] = None) -> List[AtletaOut]:
    """Get all atletas."""
    service = AtletaService(session)
    return await service.get_all()