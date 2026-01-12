# Tests

## Estructura recomendada

```
tests/
├── __init__.py
├── conftest.py          # Fixtures compartidos
├── test_main.py         # Tests de main.py
├── test_<modulo>.py     # Un archivo por módulo
└── integration/         # Tests de integración (opcional)
    └── test_api.py
```

## Buenas prácticas

### Nombrado
- Archivos: `test_<nombre_modulo>.py`
- Funciones: `test_<que_prueba>_<condicion>_<resultado_esperado>()`
- Ejemplo: `test_login_con_password_invalido_retorna_error()`

### Estructura AAA (Arrange-Act-Assert)
```python
def test_suma_dos_numeros():
    # Arrange - preparar datos
    a, b = 2, 3
    
    # Act - ejecutar
    resultado = sumar(a, b)
    
    # Assert - verificar
    assert resultado == 5
```

### Fixtures (conftest.py)
```python
import pytest

@pytest.fixture
def usuario_ejemplo():
    """Usuario de prueba reutilizable."""
    return {"nombre": "Test", "email": "test@example.com"}

# Uso en tests:
def test_algo(usuario_ejemplo):
    assert usuario_ejemplo["nombre"] == "Test"
```

### Parametrización
```python
import pytest

@pytest.mark.parametrize("entrada,esperado", [
    (1, 2),
    (2, 4),
    (3, 6),
])
def test_duplicar(entrada, esperado):
    assert duplicar(entrada) == esperado
```

## Comandos

```bash
# Ejecutar todos los tests
uv run pytest

# Con cobertura
uv run pytest --cov=src

# Solo un archivo
uv run pytest tests/test_main.py

# Verbose
uv run pytest -v
```

## Convenciones

- Un archivo de test por cada módulo de `src/`
- Tests unitarios rápidos (< 1 segundo cada uno)
- Tests de integración en carpeta separada
- Usar fixtures para evitar repetición
- Nombrar tests de forma descriptiva
