"""
Script to populate the workout_api database using direct Python package imports.
No HTTP calls required - uses the package as a library.

Usage:
    python populate_db.py
"""
import asyncio
from workout_api.services import CategoriaService, CentroTreinamentoService, AtletaService

# Same data from the original script
CATEGORIAS = [
    {"nome": "Scale"},
    {"nome": "RX"},
    {"nome": "Teens"},
    {"nome": "Masters"},
    {"nome": "Elite"},
    {"nome": "Kids"},
    {"nome": "Adaptive"},
]

CENTROS_TREINAMENTO = [
    {
        "nome": "CT King",
        "endereco": "Rua das Flores, 123, Centro",
        "proprietario": "Marcos Silva"
    },
    {
        "nome": "CT Champions",
        "endereco": "Av. Paulista, 1000, Bela Vista",
        "proprietario": "Ana Paula Costa"
    },
    {
        "nome": "CT Warriors",
        "endereco": "Rua dos Campeões, 456, Zona Sul",
        "proprietario": "Roberto Santos"
    },
    {
        "nome": "CT Evolution",
        "endereco": "Av. Independência, 789, Centro",
        "proprietario": "Juliana Mendes"
    },
    {
        "nome": "CT Strong",
        "endereco": "Rua da Força, 321, Zona Norte",
        "proprietario": "Carlos Oliveira"
    },
    {
        "nome": "CT Performance",
        "endereco": "Av. Brasil, 2000, Zona Oeste",
        "proprietario": "Patricia Lima"
    },
    {
        "nome": "CT Victory",
        "endereco": "Rua Vitória, 555, Centro",
        "proprietario": "Fernando Rocha"
    },
    {
        "nome": "CT Elite Fitness",
        "endereco": "Av. das Nações, 1500, Bairro Novo",
        "proprietario": "Luciana Ferreira"
    },
]

ATLETAS = [
    {
        "nome": "João Silva",
        "cpf": "12345678222",
        "idade": 25,
        "peso": 75.5,
        "altura": 1.75,
        "sexo": "M",
        "categoria_nome": "RX",
        "centro_treinamento_nome": "CT King"
    },
    {
        "nome": "Maria Santos",
        "cpf": "98765432109",
        "idade": 28,
        "peso": 62.3,
        "altura": 1.65,
        "sexo": "F",
        "categoria_nome": "RX",
        "centro_treinamento_nome": "CT Champions"
    },
    {
        "nome": "Pedro Oliveira",
        "cpf": "11122233344",
        "idade": 32,
        "peso": 85.0,
        "altura": 1.82,
        "sexo": "M",
        "categoria_nome": "Masters",
        "centro_treinamento_nome": "CT Warriors"
    },
    {
        "nome": "Ana Costa",
        "cpf": "55566677788",
        "idade": 22,
        "peso": 58.7,
        "altura": 1.68,
        "sexo": "F",
        "categoria_nome": "Scale",
        "centro_treinamento_nome": "CT Evolution"
    },
    {
        "nome": "Carlos Mendes",
        "cpf": "99988877766",
        "idade": 35,
        "peso": 90.5,
        "altura": 1.78,
        "sexo": "M",
        "categoria_nome": "Elite",
        "centro_treinamento_nome": "CT Strong"
    },
    {
        "nome": "Juliana Ferreira",
        "cpf": "44455566677",
        "idade": 27,
        "peso": 65.2,
        "altura": 1.70,
        "sexo": "F",
        "categoria_nome": "RX",
        "centro_treinamento_nome": "CT Performance"
    },
    {
        "nome": "Roberto Lima",
        "cpf": "33344455566",
        "idade": 29,
        "peso": 78.9,
        "altura": 1.80,
        "sexo": "M",
        "categoria_nome": "RX",
        "centro_treinamento_nome": "CT Victory"
    },
    {
        "nome": "Patricia Souza",
        "cpf": "22233344455",
        "idade": 16,
        "peso": 55.0,
        "altura": 1.62,
        "sexo": "F",
        "categoria_nome": "Teens",
        "centro_treinamento_nome": "CT Elite Fitness"
    },
    {
        "nome": "Fernando Rocha",
        "cpf": "66677788899",
        "idade": 42,
        "peso": 82.3,
        "altura": 1.76,
        "sexo": "M",
        "categoria_nome": "Masters",
        "centro_treinamento_nome": "CT King"
    },
    {
        "nome": "Luciana Alves",
        "cpf": "77788899900",
        "idade": 24,
        "peso": 60.5,
        "altura": 1.66,
        "sexo": "F",
        "categoria_nome": "Scale",
        "centro_treinamento_nome": "CT Champions"
    },
    {
        "nome": "André Barbosa",
        "cpf": "88899900011",
        "idade": 31,
        "peso": 88.7,
        "altura": 1.85,
        "sexo": "M",
        "categoria_nome": "Elite",
        "centro_treinamento_nome": "CT Warriors"
    },
    {
        "nome": "Camila Dias",
        "cpf": "10011122233",
        "idade": 26,
        "peso": 57.8,
        "altura": 1.64,
        "sexo": "F",
        "categoria_nome": "RX",
        "centro_treinamento_nome": "CT Evolution"
    },
    {
        "nome": "Gabriel Martins",
        "cpf": "20022233344",
        "idade": 12,
        "peso": 45.5,
        "altura": 1.55,
        "sexo": "M",
        "categoria_nome": "Kids",
        "centro_treinamento_nome": "CT Strong"
    },
    {
        "nome": "Beatriz Cardoso",
        "cpf": "30033344455",
        "idade": 38,
        "peso": 68.9,
        "altura": 1.69,
        "sexo": "F",
        "categoria_nome": "Masters",
        "centro_treinamento_nome": "CT Performance"
    },
    {
        "nome": "Ricardo Pereira",
        "cpf": "40044455566",
        "idade": 33,
        "peso": 92.1,
        "altura": 1.88,
        "sexo": "M",
        "categoria_nome": "Elite",
        "centro_treinamento_nome": "CT Victory"
    },
    {
        "nome": "Daniela Nunes",
        "cpf": "50055566677",
        "idade": 23,
        "peso": 59.3,
        "altura": 1.67,
        "sexo": "F",
        "categoria_nome": "Scale",
        "centro_treinamento_nome": "CT Elite Fitness"
    },
    {
        "nome": "Thiago Ramos",
        "cpf": "60066677788",
        "idade": 30,
        "peso": 80.0,
        "altura": 1.79,
        "sexo": "M",
        "categoria_nome": "RX",
        "centro_treinamento_nome": "CT King"
    },
    {
        "nome": "Mariana Torres",
        "cpf": "70077788899",
        "idade": 17,
        "peso": 56.2,
        "altura": 1.63,
        "sexo": "F",
        "categoria_nome": "Teens",
        "centro_treinamento_nome": "CT Champions"
    },
    {
        "nome": "Bruno Azevedo",
        "cpf": "80088899900",
        "idade": 45,
        "peso": 86.5,
        "altura": 1.77,
        "sexo": "M",
        "categoria_nome": "Masters",
        "centro_treinamento_nome": "CT Warriors"
    },
    {
        "nome": "Sofia Moreira",
        "cpf": "90099900011",
        "idade": 25,
        "peso": 61.8,
        "altura": 1.71,
        "sexo": "F",
        "categoria_nome": "RX",
        "centro_treinamento_nome": "CT Evolution"
    },
]


async def populate_database():
    """Populate database using direct Python API with OOP services."""
    print("=" * 60)
    print("POPULATING WORKOUT API DATABASE (DIRECT PYTHON)")
    print("=" * 60)
    
    # Initialize services
    categoria_service = CategoriaService()
    centro_service = CentroTreinamentoService()
    atleta_service = AtletaService()
    
    # Insert categorias
    print("\n=== Inserting Categorias ===")
    categorias_success = 0
    for cat_data in CATEGORIAS:
        try:
            result = await categoria_service.create(nome=cat_data['nome'])
            print(f"  ✓ Added categoria: {result.nome} (ID: {result.id})")
            categorias_success += 1
        except Exception as e:
            print(f"  ✗ Failed to add categoria {cat_data['nome']}: {e}")
    
    print(f"✓ Inserted {categorias_success}/{len(CATEGORIAS)} categorias")
    
    # Insert centros de treinamento
    print("\n=== Inserting Centros de Treinamento ===")
    centros_success = 0
    for centro_data in CENTROS_TREINAMENTO:
        try:
            result = await centro_service.create(
                nome=centro_data['nome'],
                endereco=centro_data['endereco'],
                proprietario=centro_data['proprietario']
            )
            print(f"  ✓ Added centro: {result.nome} (ID: {result.id})")
            centros_success += 1
        except Exception as e:
            print(f"  ✗ Failed to add centro {centro_data['nome']}: {e}")
    
    print(f"✓ Inserted {centros_success}/{len(CENTROS_TREINAMENTO)} centros de treinamento")
    
    # Insert atletas
    print("\n=== Inserting Atletas ===")
    atletas_success = 0
    for atleta_data in ATLETAS:
        try:
            result = await atleta_service.create(
                nome=atleta_data['nome'],
                cpf=atleta_data['cpf'],
                idade=atleta_data['idade'],
                peso=atleta_data['peso'],
                altura=atleta_data['altura'],
                sexo=atleta_data['sexo'],
                categoria_nome=atleta_data['categoria_nome'],
                centro_treinamento_nome=atleta_data['centro_treinamento_nome']
            )
            print(f"  ✓ Added atleta: {result.nome} ({atleta_data['categoria_nome']} / {atleta_data['centro_treinamento_nome']})")
            atletas_success += 1
        except Exception as e:
            print(f"  ✗ Failed to add atleta {atleta_data['nome']}: {e}")
    
    print(f"✓ Inserted {atletas_success}/{len(ATLETAS)} atletas")
    
    print("\n" + "=" * 60)
    print("✓ DATABASE POPULATION COMPLETE!")
    print("=" * 60)
    print(f"\nSummary:")
    print(f"  - Categorias: {categorias_success}/{len(CATEGORIAS)}")
    print(f"  - Centros de Treinamento: {centros_success}/{len(CENTROS_TREINAMENTO)}")
    print(f"  - Atletas: {atletas_success}/{len(ATLETAS)}")
    print("=" * 60)


if __name__ == "__main__":
    asyncio.run(populate_database())
