#!/usr/bin/env python3
"""
Comprehensive Software House Example
Demonstrates all features of the Software House Prompt Engineering Agent
"""

import os
from dotenv import load_dotenv
from src.simple_agent import SimplePromptAgent
from src.software_house_agent import SoftwareHouseAgent

# Load environment variables
load_dotenv()

def main():
    """Run comprehensive examples of all software house agent features."""
    print("🏢 Software House Prompt Engineering Agent - Comprehensive Example")
    print("=" * 70)
    
    try:
        # Initialize agents
        prompt_agent = SimplePromptAgent()
        software_agent = SoftwareHouseAgent()
        
        print("\n🚀 Starting comprehensive demonstration...")
        
        # 1. Prompt Engineering Examples
        print("\n1. 📝 PROMPT ENGINEERING EXAMPLES")
        print("=" * 40)
        
        # Prompt Analysis
        print("\n1.1 Prompt Analysis")
        test_prompts = [
            "Write about AI",
            "Create a comprehensive guide to machine learning for beginners",
            "Design a database schema for an e-commerce platform"
        ]
        
        for i, prompt in enumerate(test_prompts, 1):
            print(f"\nAnalyzing Prompt {i}: {prompt}")
            analysis = prompt_agent.analyze_prompt(prompt, "For software development documentation")
            print(f"  Clarity: {analysis['clarity_score']}/10")
            print(f"  Specificity: {analysis['specificity_score']}/10")
            print(f"  Suggestions: {len(analysis['suggestions'])} found")
        
        # Prompt Optimization
        print("\n1.2 Prompt Optimization")
        original_prompt = "Write about AI"
        optimized = prompt_agent.optimize_prompt(
            original_prompt,
            "Too vague, lacks context and audience",
            "Create a specific, actionable prompt for technical documentation"
        )
        print(f"Original: {original_prompt}")
        print(f"Optimized: {optimized}")
        
        # A/B Testing
        print("\n1.3 A/B Testing")
        prompt_a = "Write about AI"
        prompt_b = "Create a comprehensive guide to artificial intelligence for software developers, covering key concepts, practical applications, and implementation examples"
        comparison = prompt_agent.compare_prompts(prompt_a, prompt_b, "Generate technical content")
        print(f"Prompt A: {prompt_a}")
        print(f"Prompt B: {prompt_b}")
        print(f"Clearer prompt: {comparison['clearer_prompt']}")
        
        # 2. Software House Specializations
        print("\n2. 🏢 SOFTWARE HOUSE SPECIALIZATIONS")
        print("=" * 40)
        
        # Technical Specifications
        print("\n2.1 Technical Specifications")
        tech_spec = software_agent.generate_technical_spec(
            "AI-powered recommendation system",
            "Personalized product recommendations based on user behavior and preferences",
            "Python, TensorFlow, FastAPI, PostgreSQL, Redis"
        )
        print("✅ Technical specification generated")
        
        # Project Proposals
        print("\n2.2 Project Proposals")
        proposal = software_agent.create_project_proposal(
            "InnovateTech Solutions",
            "Development of a comprehensive AI-powered analytics dashboard for business intelligence",
            "$100,000 - $150,000"
        )
        print("✅ Project proposal generated")
        
        # Code Documentation
        print("\n2.3 Code Documentation")
        code_snippet = """
class RecommendationEngine:
    def __init__(self, model_path: str):
        self.model = self.load_model(model_path)
        self.user_profiles = {}
    
    def get_recommendations(self, user_id: str, limit: int = 10) -> List[Dict]:
        profile = self.get_user_profile(user_id)
        predictions = self.model.predict(profile)
        return self.format_recommendations(predictions, limit)
        """
        
        documentation = software_agent.generate_code_documentation(
            code_snippet,
            "Python",
            "AI recommendation engine class for generating personalized product suggestions"
        )
        print("✅ Code documentation generated")
        
        # Client Communication
        print("\n2.4 Client Communication")
        communication = software_agent.create_client_communication(
            "Project timeline needs to be extended by 2 weeks due to additional requirements",
            "Enterprise",
            "Professional"
        )
        print("✅ Client communication generated")
        
        # Test Cases
        print("\n2.5 Test Cases")
        test_cases = software_agent.generate_test_cases(
            "User authentication system with OAuth2 and JWT tokens",
            "Integration"
        )
        print("✅ Test cases generated")
        
        # Development Estimates
        print("\n2.6 Development Estimates")
        estimate = software_agent.create_development_estimate(
            "Build a real-time chat application with WebSocket support",
            "Complex",
            "3 developers"
        )
        print("✅ Development estimate generated")
        print(f"  Estimated hours: {estimate['estimated_hours']}")
        print(f"  Timeline: {estimate['timeline_days']} days")
        print(f"  Complexity: {estimate['complexity_analysis']}")
        
        # Deployment Guides
        print("\n2.7 Deployment Guides")
        deployment_guide = software_agent.generate_deployment_guide(
            "AI Analytics Platform",
            "Production",
            "Docker, Kubernetes, AWS, PostgreSQL, Redis"
        )
        print("✅ Deployment guide generated")
        
        # Project Status Reports
        print("\n2.8 Project Status Reports")
        status_report = software_agent.create_project_status_report(
            "E-commerce Platform Redesign",
            "Phase 2 development in progress, 70% complete",
            "User authentication (completed), Product catalog (in progress), Payment integration (pending)"
        )
        print("✅ Project status report generated")
        
        # Technical Interview Questions
        print("\n2.9 Technical Interview Questions")
        interview_questions = software_agent.generate_technical_interview_questions(
            "Senior Python Developer",
            "Senior",
            "Backend development, API design, database optimization, cloud deployment"
        )
        print("✅ Technical interview questions generated")
        
        # 3. Save all results to files
        print("\n3. 💾 SAVING RESULTS")
        print("=" * 40)
        
        results = {
            "technical_specification.txt": tech_spec,
            "project_proposal.txt": proposal,
            "code_documentation.txt": documentation,
            "client_communication.txt": communication,
            "test_cases.txt": test_cases,
            "development_estimate.txt": f"Raw Response: {estimate['raw_response']}\n\nParsed Data: {estimate}",
            "deployment_guide.txt": deployment_guide,
            "project_status_report.txt": status_report,
            "interview_questions.txt": interview_questions,
            "prompt_analysis.txt": f"Analysis Results:\n{analysis}\n\nOptimized Prompt:\n{optimized}\n\nA/B Comparison:\n{comparison}",
        }
        
        for filename, content in results.items():
            with open(filename, "w") as f:
                f.write(content)
            print(f"✅ Saved: {filename}")
        
        print("\n🎉 COMPREHENSIVE DEMONSTRATION COMPLETED!")
        print("=" * 70)
        print("📁 All results have been saved to individual files.")
        print("🔧 You can now use these examples as templates for your own projects.")
        print("🚀 Run 'python interactive_prompt_agent.py' for interactive mode.")
        
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        print("Make sure you have set up your OpenAI API key in the .env file.")

if __name__ == "__main__":
    main() 