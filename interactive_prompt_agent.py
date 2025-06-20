#!/usr/bin/env python3
"""
Interactive Software House Prompt Engineering Agent
Asks what you need, generates prompts, allows refinement, and provides suggestions
"""

import os
from dotenv import load_dotenv
from src.software_house_agent import SoftwareHouseAgent
from src.simple_agent import SimplePromptAgent

# Load environment variables
load_dotenv()

def get_user_requirements():
    """Get user requirements through interactive prompts."""
    print("🏢 Interactive Software House Prompt Engineering Agent")
    print("=" * 60)
    print("What would you like me to help you with today?\n")
    
    # Main categories
    categories = {
        "1": "Prompt Engineering & Analysis",
        "2": "Technical Specifications & Architecture", 
        "3": "Project Proposals & Client Communication", 
        "4": "Code Documentation & Testing",
        "5": "Development Estimates & Project Management",
        "6": "Deployment Guides & DevOps",
        "7": "Technical Interview Questions & Hiring",
        "8": "Custom Task"
    }
    
    print("Available categories:")
    for key, value in categories.items():
        print(f"{key}. {value}")
    
    while True:
        choice = input("\nEnter your choice (1-8): ").strip()
        if choice in categories:
            return categories[choice]
        print("❌ Invalid choice. Please enter 1-8.")

def get_specific_details(category):
    """Get specific details based on the chosen category."""
    print(f"\n📋 {category}")
    print("-" * 30)
    
    details = {}
    
    if "Prompt Engineering" in category:
        details["prompt"] = input("Enter the prompt to analyze: ")
        details["context"] = input("Context (optional): ")
        
    elif "Technical Specifications" in category:
        details["project_type"] = input("What type of project? (e.g., e-commerce, mobile app, CRM): ")
        details["requirements"] = input("What are the main requirements? ")
        details["tech_stack"] = input("Preferred tech stack? (optional): ")
        
    elif "Project Proposals" in category:
        details["client_name"] = input("Client name: ")
        details["project_scope"] = input("Project scope/description: ")
        details["budget_range"] = input("Budget range: ")
        
    elif "Code Documentation" in category:
        details["code_snippet"] = input("Paste your code here: ")
        details["language"] = input("Programming language: ")
        details["purpose"] = input("What does this code do? ")
        
    elif "Development Estimates" in category:
        details["task_description"] = input("Describe the development task: ")
        details["complexity_level"] = input("Complexity level (Simple/Moderate/Complex): ")
        details["team_size"] = input("Team size: ")
        
    elif "Deployment Guides" in category:
        details["project_name"] = input("Project name: ")
        details["environment"] = input("Environment (Development/Staging/Production): ")
        details["tech_stack"] = input("Tech stack: ")
        
    elif "Status Reports" in category:
        details["project_name"] = input("Project name: ")
        details["current_status"] = input("Current status: ")
        details["milestones"] = input("Key milestones: ")
        
    elif "Interview Questions" in category:
        details["position"] = input("Position title: ")
        details["skill_level"] = input("Skill level (Junior/Mid/Senior): ")
        details["focus_areas"] = input("Focus areas: ")
        
    elif "Client Communication" in category:
        details["situation"] = input("Describe the situation: ")
        details["client_type"] = input("Client type (Startup/Enterprise/Small Business): ")
        details["tone"] = input("Tone (Professional/Reassuring/Formal): ")
        
    elif "Test Cases" in category:
        details["feature_description"] = input("Feature description: ")
        details["testing_type"] = input("Testing type (Unit/Integration/System): ")
        
    else:  # Custom Task
        details["custom_task"] = input("Describe what you need: ")
    
    return details

def generate_prompts(category, details):
    """Generate multiple prompt options based on category and details."""
    print(f"\n🎯 Generating prompts for: {category}")
    print("-" * 40)
    
    prompts = []
    
    if "Prompt Engineering" in category:
        prompts = [
            f"Analyze this prompt for effectiveness: {details.get('prompt', '')}",
            f"Optimize this prompt: {details.get('prompt', '')}",
            f"Compare this prompt with alternatives: {details.get('prompt', '')}"
        ]
        
    elif "Technical Specifications" in category:
        prompts = [
            f"Generate a comprehensive technical specification for a {details.get('project_type', 'software')} project with requirements: {details.get('requirements', '')}",
            f"Create a detailed system architecture document for {details.get('project_type', 'project')} using {details.get('tech_stack', 'modern technologies')}",
            f"Design a technical blueprint for {details.get('project_type', 'application')} including database schema, API design, and security considerations"
        ]
        
    elif "Project Proposals" in category:
        prompts = [
            f"Create a professional project proposal for {details.get('client_name', 'client')} for {details.get('project_scope', 'project')} with budget {details.get('budget_range', 'range')}",
            f"Write a compelling business proposal for {details.get('client_name', 'client')} covering {details.get('project_scope', 'project scope')}",
            f"Generate a detailed project proposal document for {details.get('client_name', 'client')} including timeline, deliverables, and pricing"
        ]
        
    elif "Code Documentation" in category:
        prompts = [
            f"Generate comprehensive documentation for this {details.get('language', 'code')} code: {details.get('code_snippet', '')}",
            f"Create professional documentation explaining the purpose and usage of this {details.get('language', 'code')}",
            f"Write detailed technical documentation for this code including parameters, return values, and examples"
        ]
        
    elif "Development Estimates" in category:
        prompts = [
            f"Provide a detailed development estimate for: {details.get('task_description', 'task')} with {details.get('complexity_level', 'complexity')} complexity",
            f"Estimate development time and resources for {details.get('task_description', 'task')} with team size {details.get('team_size', 'team')}",
            f"Create a comprehensive project estimation including timeline, costs, and resource requirements for {details.get('task_description', 'task')}"
        ]
        
    elif "Deployment Guides" in category:
        prompts = [
            f"Create a step-by-step deployment guide for {details.get('project_name', 'project')} on {details.get('environment', 'environment')}",
            f"Generate a comprehensive deployment manual for {details.get('project_name', 'project')} using {details.get('tech_stack', 'tech stack')}",
            f"Write a detailed DevOps guide for deploying {details.get('project_name', 'project')} including troubleshooting and rollback procedures"
        ]
        
    elif "Status Reports" in category:
        prompts = [
            f"Generate a professional project status report for {details.get('project_name', 'project')} with current status: {details.get('current_status', 'status')}",
            f"Create a detailed progress report for {details.get('project_name', 'project')} covering milestones: {details.get('milestones', 'milestones')}",
            f"Write a comprehensive status update for {details.get('project_name', 'project')} suitable for client presentation"
        ]
        
    elif "Interview Questions" in category:
        prompts = [
            f"Create technical interview questions for {details.get('position', 'position')} at {details.get('skill_level', 'skill level')} level",
            f"Generate comprehensive interview questions for {details.get('position', 'position')} focusing on {details.get('focus_areas', 'skills')}",
            f"Design a complete interview guide for {details.get('position', 'position')} including technical and behavioral questions"
        ]
        
    elif "Client Communication" in category:
        prompts = [
            f"Write a professional {details.get('tone', 'professional')} communication for {details.get('client_type', 'client')} about {details.get('situation', 'situation')}",
            f"Create a client email addressing {details.get('situation', 'situation')} for {details.get('client_type', 'client type')} client",
            f"Generate a professional message to {details.get('client_type', 'client')} regarding {details.get('situation', 'situation')}"
        ]
        
    elif "Test Cases" in category:
        prompts = [
            f"Generate comprehensive {details.get('testing_type', 'test')} test cases for {details.get('feature_description', 'feature')}",
            f"Create detailed test scenarios for {details.get('feature_description', 'feature')} including edge cases",
            f"Design a complete test plan for {details.get('feature_description', 'feature')} with {details.get('testing_type', 'testing')} approach"
        ]
        
    else:  # Custom Task
        custom_task = details.get('custom_task', '')
        prompts = [
            f"Help me with: {custom_task}",
            f"Provide detailed assistance for: {custom_task}",
            f"Create a comprehensive solution for: {custom_task}"
        ]
    
    return prompts

def refine_prompt(prompt):
    """Allow user to refine the selected prompt."""
    print(f"\n📝 Selected Prompt: {prompt}")
    print("-" * 50)
    
    print("Would you like to refine this prompt?")
    print("1. Add more specific details")
    print("2. Change the tone/style")
    print("3. Add specific requirements")
    print("4. Use as is")
    
    choice = input("\nEnter your choice (1-4): ").strip()
    
    if choice == "1":
        additional_details = input("Add more specific details: ")
        return f"{prompt} Additional details: {additional_details}"
    elif choice == "2":
        tone = input("What tone/style would you prefer? ")
        return f"{prompt} Use a {tone} tone/style."
    elif choice == "3":
        requirements = input("Add specific requirements: ")
        return f"{prompt} Specific requirements: {requirements}"
    else:
        return prompt

def main():
    """Main interactive function."""
    try:
        # Initialize agents
        software_agent = SoftwareHouseAgent()
        prompt_agent = SimplePromptAgent()
        
        while True:
            # Get user requirements
            category = get_user_requirements()
            details = get_specific_details(category)
            
            # Generate prompt options
            prompts = generate_prompts(category, details)
            
            # Display prompt options
            print("\n📝 Generated Prompt Options:")
            for i, prompt in enumerate(prompts, 1):
                print(f"{i}. {prompt}")
            
            # Let user select or create custom prompt
            print("\nOptions:")
            print("1-3. Select one of the generated prompts")
            print("4. Create custom prompt")
            print("5. Exit")
            
            choice = input("\nEnter your choice (1-5): ").strip()
            
            if choice == "5":
                print("👋 Goodbye!")
                break
            elif choice == "4":
                custom_prompt = input("Enter your custom prompt: ")
                selected_prompt = custom_prompt
            elif choice in ["1", "2", "3"]:
                selected_prompt = prompts[int(choice) - 1]
            else:
                print("❌ Invalid choice. Please try again.")
                continue
            
            # Refine the prompt
            final_prompt = refine_prompt(selected_prompt)
            
            # Execute the prompt
            print(f"\n🚀 Executing prompt...")
            print("-" * 50)
            
            try:
                if "Prompt Engineering" in category:
                    # Use prompt engineering agent
                    if "analyze" in final_prompt.lower():
                        result = prompt_agent.analyze_prompt(details.get('prompt', ''), details.get('context', ''))
                        print("📊 Analysis Results:")
                        print(f"Clarity Score: {result['clarity_score']}/10")
                        print(f"Specificity Score: {result['specificity_score']}/10")
                        print(f"Suggestions: {', '.join(result['suggestions'])}")
                        print(f"\nDetailed Analysis:\n{result['analysis']}")
                    elif "optimize" in final_prompt.lower():
                        issues = input("What issues do you see with the prompt? ")
                        goal = input("What's your optimization goal? ")
                        result = prompt_agent.optimize_prompt(details.get('prompt', ''), issues, goal)
                        print(f"\n✅ Optimized Prompt:\n{result}")
                    else:
                        result = prompt_agent.generate_prompt("role_based", role="software engineer", task="analyze prompt", input_text=final_prompt)
                        print(f"\n🤖 AI Response:\n{result}")
                else:
                    # Use software house agent
                    result = software_agent.llm.predict(final_prompt)
                    print(f"\n🤖 AI Response:\n{result}")
                
                # Save to file
                filename = f"software_house_output_{category.lower().replace(' ', '_')}.txt"
                with open(filename, 'w') as f:
                    f.write(f"Category: {category}\n")
                    f.write(f"Prompt: {final_prompt}\n")
                    f.write(f"Response: {result}\n")
                
                print(f"\n💾 Results saved to: {filename}")
                
            except Exception as e:
                print(f"❌ Error: {str(e)}")
            
            # Ask if user wants to continue
            print("\n" + "="*60)
            continue_choice = input("Would you like to continue? (y/n): ").strip().lower()
            if continue_choice != 'y':
                print("👋 Goodbye!")
                break
                
    except KeyboardInterrupt:
        print("\n\n👋 Goodbye!")
    except Exception as e:
        print(f"❌ Unexpected error: {str(e)}")

if __name__ == "__main__":
    main() 