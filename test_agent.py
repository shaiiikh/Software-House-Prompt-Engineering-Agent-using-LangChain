#!/usr/bin/env python3
"""
Test Script for Software House Prompt Engineering Agent
Basic functionality testing
"""

import os
from dotenv import load_dotenv
from src.simple_agent import SimplePromptAgent
from src.software_house_agent import SoftwareHouseAgent

# Load environment variables
load_dotenv()

def test_prompt_agent():
    """Test the simple prompt agent functionality."""
    print("🧪 Testing Simple Prompt Agent...")
    
    try:
        agent = SimplePromptAgent()
        
        # Test prompt analysis
        print("  ✓ Testing prompt analysis...")
        analysis = agent.analyze_prompt("Write about AI", "For technical documentation")
        assert isinstance(analysis, dict)
        assert 'clarity_score' in analysis
        assert 'specificity_score' in analysis
        print("    ✓ Prompt analysis working")
        
        # Test prompt optimization
        print("  ✓ Testing prompt optimization...")
        optimized = agent.optimize_prompt(
            "Write about AI",
            "Too vague",
            "Make it specific for developers"
        )
        assert isinstance(optimized, str)
        assert len(optimized) > 0
        print("    ✓ Prompt optimization working")
        
        print("  ✅ Simple Prompt Agent tests passed!")
        return True
        
    except Exception as e:
        print(f"  ❌ Simple Prompt Agent test failed: {str(e)}")
        return False

def test_software_house_agent():
    """Test the software house agent functionality."""
    print("🧪 Testing Software House Agent...")
    
    try:
        agent = SoftwareHouseAgent()
        
        # Test technical specification generation
        print("  ✓ Testing technical specification generation...")
        spec = agent.generate_technical_spec(
            "web application",
            "Basic requirements",
            "Python, Django"
        )
        assert isinstance(spec, str)
        assert len(spec) > 0
        print("    ✓ Technical specification generation working")
        
        # Test project proposal generation
        print("  ✓ Testing project proposal generation...")
        proposal = agent.create_project_proposal(
            "Test Client",
            "Test project",
            "$10,000"
        )
        assert isinstance(proposal, str)
        assert len(proposal) > 0
        print("    ✓ Project proposal generation working")
        
        # Test development estimate
        print("  ✓ Testing development estimate...")
        estimate = agent.create_development_estimate(
            "Simple feature",
            "Simple",
            "1 developer"
        )
        assert isinstance(estimate, dict)
        assert 'estimated_hours' in estimate
        print("    ✓ Development estimate working")
        
        print("  ✅ Software House Agent tests passed!")
        return True
        
    except Exception as e:
        print(f"  ❌ Software House Agent test failed: {str(e)}")
        return False

def test_configuration():
    """Test configuration setup."""
    print("🧪 Testing Configuration...")
    
    try:
        from src.config import Config
        
        # Test configuration validation
        print("  ✓ Testing configuration validation...")
        Config.validate()
        print("    ✓ Configuration validation working")
        
        # Test model config
        print("  ✓ Testing model configuration...")
        model_config = Config.get_model_config()
        assert isinstance(model_config, dict)
        assert 'model_name' in model_config
        print("    ✓ Model configuration working")
        
        print("  ✅ Configuration tests passed!")
        return True
        
    except Exception as e:
        print(f"  ❌ Configuration test failed: {str(e)}")
        return False

def main():
    """Run all tests."""
    print("🏢 Software House Prompt Engineering Agent - Test Suite")
    print("=" * 60)
    
    # Check if API key is set
    if not os.getenv("OPENAI_API_KEY"):
        print("❌ OPENAI_API_KEY not found in environment variables.")
        print("Please set up your .env file with your OpenAI API key.")
        return
    
    tests = [
        test_configuration,
        test_prompt_agent,
        test_software_house_agent,
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
        print()
    
    print("📊 Test Results:")
    print(f"  Passed: {passed}/{total}")
    print(f"  Failed: {total - passed}/{total}")
    
    if passed == total:
        print("🎉 All tests passed! The agent is ready to use.")
    else:
        print("⚠️  Some tests failed. Please check the error messages above.")

if __name__ == "__main__":
    main() 