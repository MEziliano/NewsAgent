"""
Test file to verify Ollama LLM connection and basic functionality.
"""

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def test_ollama_basic():
    """Test basic Ollama connection using langchain_ollama"""
    print("=" * 60)
    print("Testing Ollama LLM Connection")
    print("=" * 60)
    
    try:
        from langchain_ollama import OllamaLLM
        
        model_name = os.getenv("OLLAMA_MODEL", "llama3.2:3b")
        print("\n✓ langchain_ollama imported successfully")
        print(f"✓ Using model: {model_name}")
        
        # Initialize the LLM
        llm = OllamaLLM(model=model_name)
        print("✓ OllamaLLM initialized")
        
        # Test with a simple prompt
        print("\n" + "-" * 60)
        print("Testing with a simple prompt...")
        print("-" * 60)
        
        test_prompt = "Olá! Qual é a capital da França? Responda em uma frase."
        print(f"\nPrompt: {test_prompt}\n")
        
        response = llm.invoke(test_prompt)
        print(f"Response:\n{response}")
        
        print("\n" + "-" * 60)
        print("✓ Ollama is working correctly!")
        print("-" * 60)
        
    except ImportError as e:
        print(f"✗ Error importing langchain_ollama: {e}")
        print("Install it with: pip install langchain-ollama")
    except Exception as e:
        print(f"✗ Error: {e}")
        print("\nMake sure Ollama is running and accessible at localhost:11434")


def test_ollama_streaming():
    """Test Ollama with streaming"""
    print("\n" + "=" * 60)
    print("Testing Ollama with Streaming")
    print("=" * 60)
    
    try:
        from langchain_ollama import OllamaLLM
        
        model_name = os.getenv("OLLAMA_MODEL", "llama3.2:3b")
        llm = OllamaLLM(model=model_name)
        
        print(f"\nStreaming response from {model_name}:\n")
        
        test_prompt = "Liste 3 curiosidades sobre tecnologia em formato numerado."
        
        # Stream the response
        for chunk in llm.stream(test_prompt):
            print(chunk, end="", flush=True)
        
        print("\n\n✓ Streaming completed!")
        
    except Exception as e:
        print(f"✗ Error during streaming: {e}")


def test_ollama_list_models():
    """Test listing available models via API"""
    print("\n" + "=" * 60)
    print("Checking Ollama API")
    print("=" * 60)
    
    try:
        import requests
        
        print("\nTesting connection to Ollama API (localhost:11434)...\n")
        
        response = requests.get("http://localhost:11434/api/tags")
        
        if response.status_code == 200:
            models = response.json()
            print("✓ Connected to Ollama API!")
            print("\nAvailable models:")
            
            if models.get("models"):
                for model in models["models"]:
                    print(f"  - {model.get('name', 'Unknown')}")
            else:
                print("  No models found. Please pull a model first.")
                print("  Example: ollama pull llama3.2:3b")
        else:
            print(f"✗ Ollama API returned status code: {response.status_code}")
            
    except requests.exceptions.ConnectionError:
        print("✗ Cannot connect to Ollama API at localhost:11434")
        print("\nMake sure Ollama is running:")
        print("  1. Download from: https://ollama.ai")
        print("  2. Run: ollama serve")
        print("  3. In another terminal, pull a model: ollama pull llama3.2:3b")
    except Exception as e:
        print(f"✗ Error: {e}")


if __name__ == "__main__":
    print("\n")
    print("╔" + "=" * 58 + "╗")
    print("║" + " " * 15 + "OLLAMA LLM CONNECTION TEST" + " " * 17 + "║")
    print("╚" + "=" * 58 + "╝")
    
    # Run all tests
    test_ollama_list_models()
    test_ollama_basic()
    test_ollama_streaming()
    
    print("\n" + "=" * 60)
    print("Tests completed!")
    print("=" * 60 + "\n")
