{% if cookiecutter.include_examples %}
"""
Basic usage examples for {{ cookiecutter.project_name }}

This module demonstrates the core functionality and basic usage patterns.
"""

from {{ cookiecutter.__package_name }} import hello_world{% if cookiecutter.include_async %}, async_hello_world{% endif %}
from {{ cookiecutter.__package_name }}.config import get_config, Config
from {{ cookiecutter.__package_name }}.core import {{ cookiecutter.__package_name.title().replace('_', '') }}Base
{% if cookiecutter.include_async %}import asyncio{% endif %}


def basic_usage():
    """Demonstrate basic functionality."""
    print("=== Basic Usage Examples ===\n")
    
    # Basic hello world
    result = hello_world()
    print(f"Basic greeting: {result}")
    
    # Custom greeting
    result = hello_world("{{ cookiecutter.project_name }}")
    print(f"Custom greeting: {result}")
    
    # Using the base class
    base = {{ cookiecutter.__package_name.title().replace('_', '') }}Base({"greeting_target": "Examples"})
    print(f"Base class: {base}")


def configuration_example():
    """Demonstrate configuration usage."""
    print("\n=== Configuration Examples ===\n")
    
    # Get default configuration
    config = get_config()
    print(f"App name: {config.app_name}")
    print(f"Version: {config.version}")
    print(f"Environment: {config.environment}")
    print(f"Debug mode: {config.debug}")
    
    # Create custom configuration
    custom_config = Config(
        debug=True,
        log_level="DEBUG",
        environment="development"
    )
    print(f"\nCustom config - Debug: {custom_config.debug}")
    print(f"Custom config - Environment: {custom_config.environment}")
    
    # Environment checks
    print(f"Is development: {custom_config.is_development()}")
    print(f"Is production: {custom_config.is_production()}")


{% if cookiecutter.include_async %}
async def async_example():
    """Demonstrate async functionality."""
    print("\n=== Async Examples ===\n")
    
    # Basic async greeting
    result = await async_hello_world("Async World")
    print(f"Async greeting: {result}")
    
    # Multiple async operations
    tasks = [
        async_hello_world(f"User {i}")
        for i in range(3)
    ]
    
    results = await asyncio.gather(*tasks)
    print("Multiple async greetings:")
    for i, result in enumerate(results, 1):
        print(f"  {i}. {result}")
{% endif %}


def main():
    """Run all examples."""
    print("{{ cookiecutter.project_name }} - Usage Examples")
    print("=" * 50)
    
    # Run synchronous examples
    basic_usage()
    configuration_example()
    
    {% if cookiecutter.include_async %}
    # Run async examples
    asyncio.run(async_example())
    {% endif %}
    
    print("\n=== Examples Complete ===")


if __name__ == "__main__":
    main()
{% endif %}