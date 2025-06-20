#!/usr/bin/env python3
"""
Simple Example for Software House Prompt Engineering Agent
Demonstrates basic functionality
"""

import os
from dotenv import load_dotenv
from src.simple_agent import SimplePromptAgent
from src.software_house_agent import SoftwareHouseAgent

# Load environment variables
load_dotenv()

def main():
    """Run simple examples of the prompt engineering agent."""
    print("🏢 Software House Prompt Engineering Agent - Simple Example")
    print("=" * 60)
    
    try:
        # Initialize agents
        prompt_agent = SimplePromptAgent()
        software_agent = SoftwareHouseAgent()
        
        print("\n1. 📝 Prompt Analysis Example")
        print("-" * 30)
        
        test_prompt = "Write about AI"
        analysis = prompt_agent.analyze_prompt(test_prompt, "For a technical blog post")
        
        print(f"Original Prompt: {test_prompt}")
        print(f"Clarity Score: {analysis['clarity_score']}/10")
        print(f"Specificity Score: {analysis['specificity_score']}/10")
        print(f"Suggestions: {', '.join(analysis['suggestions'])}")
        
        print("\n2. 🔧 Prompt Optimization Example")
        print("-" * 30)
        
        optimized = prompt_agent.optimize_prompt(
            "Write about AI",
            "Too vague, lacks specificity",
            "Create a clear, specific prompt for a technical audience"
        )
        
        print(f"Optimized Prompt: {optimized}")
        
        print("\n3. 🏗️ Technical Specification Example")
        print("-" * 30)
        
        tech_spec = software_agent.generate_technical_spec(
            "e-commerce platform",
            "Online store with payment processing, inventory management, and customer reviews",
            "React, Node.js, PostgreSQL"
        )
        
        print("Technical Specification Generated!")
        print("(Full specification saved to file)")
        
        # Save to file
        with open("technical_spec_example.txt", "w") as f:
            f.write(tech_spec)
        
        print("\n4. 📋 Project Proposal Example")
        print("-" * 30)
        
        proposal = software_agent.create_project_proposal(
            "TechCorp Inc.",
            "AI-powered customer service chatbot",
            "$50,000 - $75,000"
        )
        
        print("Project Proposal Generated!")
        print("(Full proposal saved to file)")
        
        # Save to file
        with open("project_proposal_example.txt", "w") as f:
            f.write(proposal)
        
        print("\n5. 📚 Code Documentation Example")
        print("-" * 30)
        
        code_snippet = """
def calculate_total(items, tax_rate=0.1):
    subtotal = sum(item['price'] for item in items)
    tax = subtotal * tax_rate
    return subtotal + tax
        """
        
        documentation = software_agent.generate_code_documentation(
            code_snippet,
            "Python",
            "Calculate total price including tax for a list of items"
        )
        
        print("Code Documentation Generated!")
        print("(Full documentation saved to file)")
        
        # Save to file
        with open("code_documentation_example.txt", "w") as f:
            f.write(documentation)
        
        print("\n✅ All examples completed successfully!")
        print("📁 Check the generated files for full results:")
        print("   - technical_spec_example.txt")
        print("   - project_proposal_example.txt")
        print("   - code_documentation_example.txt")
        
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        print("Make sure you have set up your OpenAI API key in the .env file.")

if __name__ == "__main__":
    main() 