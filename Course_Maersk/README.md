# OpenAI Course - Complete Learning Path

Welcome to the comprehensive OpenAI course designed to take you from basic prompting to advanced AI tool integration. This course is structured in three progressive modules, each building upon the previous knowledge.

## 📋 Table of Contents
- [Course Overview](#course-overview)
- [Prerequisites](#prerequisites)
- [Setup Instructions](#setup-instructions)
- [Course Structure](#course-structure)
  - [Module 1: Foundation OpenAI Concepts](#module-1-foundation-openai-concepts-open_ai_courses)
  - [Module 2: Advanced Function Calling](#module-2-advanced-function-calling-function_calling_openai)
  - [Module 3: Next-Generation OpenAI Features](#module-3-next-generation-openai-features-open_ai_new)
- [Learning Path](#learning-path)
- [Troubleshooting](#troubleshooting)
- [Additional Resources](#additional-resources)

## 🎯 Course Overview

This course covers the complete spectrum of OpenAI's capabilities, from basic chat interactions to advanced tool integrations including audio, image generation, reasoning models, and the latest GPT-5 features. Perfect for developers, researchers, and AI enthusiasts looking to master OpenAI's ecosystem with real-world logistics and supply chain use cases.

**What You'll Learn:**
- Fundamental prompting techniques and best practices
- Advanced prompt engineering with chain-of-thought reasoning
- Custom function calling and structured outputs
- Audio processing and generation
- Image generation and analysis
- Advanced reasoning capabilities
- Tool integration (web search, code interpreter, file search)
- Chat applications with memory management

## 🔧 Prerequisites

- **Python Knowledge**: Intermediate level (functions, classes, file handling)
- **API Understanding**: Basic knowledge of REST APIs and JSON
- **Environment Setup**: Familiarity with virtual environments and package management
- **OpenAI Account**: Active OpenAI account with API access

## ⚙️ Setup Instructions

### 1. Clone/Download the Repository
```bash
git clone <your-repository-url>
cd Course_Maersk
```

### 2. Create Virtual Environment
```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install openai python-dotenv pydantic
```

### 4. Environment Configuration
Create a `.env` file in the root directory:
```env
OPENAI_API_KEY=your_openai_api_key_here
```

**⚠️ Security Note**: Never commit your API keys to version control. The provided examples may contain placeholder keys that should be replaced with your actual keys.

## 📚 Course Structure

### Module 1: Foundation OpenAI Concepts (`open_ai_courses/`)

This module establishes the fundamentals of working with OpenAI's API and effective prompting techniques.

#### **Lesson 0: Basic Connection & Prompting** (`lesson0.py`)
- **Objective**: Learn to connect to OpenAI API and perform basic prompting
- **Key Concepts**:
  - API authentication and client setup
  - Basic prompt construction
  - String interpolation for dynamic prompts
  - Temperature settings and model selection
- **Practical Example**: Baby name suggestion app based on religion, country, and gender
- **Skills Gained**: Foundation API usage, prompt parameterization

#### **Lesson 1: Advanced Prompting Techniques** (`lesson1.py`)
- **Objective**: Master structured prompting and output formatting
- **Key Concepts**:
  - Principle 1: Clear and specific instructions
  - Delimiter usage (```, ---, < >, XML tags)
  - Structured output requests (JSON format)
  - Condition checking and validation
  - Few-shot prompting with examples
- **Practical Examples**:
  - Container and ship spare parts inventory management
  - Email writing with consistent style for logistics operations
- **Skills Gained**: Professional prompt engineering, structured data extraction

#### **Lesson 3: Chain-of-Thought Reasoning** (`Lesson3.py`)
- **Objective**: Implement advanced reasoning patterns
- **Key Concepts**:
  - Principle 2: Give models time to think
  - Step-by-step analysis frameworks
  - Self-evaluation techniques
  - Complex problem decomposition
- **Practical Examples**:
  - Customer service call analysis for logistics support with JSON output
  - Mathematical problem verification for shipping calculations
- **Skills Gained**: Complex analysis workflows, quality assurance patterns

#### **Lesson 4: Iterative Development** (`lesson4.py`)
- **Objective**: Learn prompt optimization strategies
- **Key Concepts**: Iterative prompt refinement process
- **Skills Gained**: Prompt debugging and optimization

#### **Chat Applications**
- **Basic Chat** (`chat_demo.py`): Simple stateless chat interface
- **Memory-Enabled Chat** (`chat_with_memory.py`): Conversation history management

### Module 2: Advanced Function Calling (`Function_Calling_OpenAi/`)

This module focuses on extending AI capabilities through custom functions and structured outputs.

#### **Custom Function Calling** (`lesson_function_calling.py`)
- **Objective**: Create and integrate custom tools with OpenAI
- **Key Concepts**:
  - JSON Schema for tool definition
  - Function call lifecycle management
  - Input/output handling
  - Multi-turn conversations with tools
- **Practical Example**: Shipment tracking status system
- **Skills Gained**: Tool integration, API orchestration

#### **Structured Output Parsing** (`lesson_structured_output.py`)
- **Objective**: Extract structured data using Pydantic models
- **Key Concepts**:
  - Pydantic BaseModel integration
  - Type-safe data extraction
  - Response parsing vs. creation
- **Practical Example**: Container booking extraction
- **Skills Gained**: Data modeling, type-safe parsing

### Module 3: Next-Generation OpenAI Features (`open_ai_new/`)

This module explores cutting-edge OpenAI capabilities and the latest API features.

#### **GPT-5 Basics** (`lesson_gpt5.py`)
- **Objective**: Utilize the latest GPT-5 model capabilities
- **Key Concepts**: GPT-5 nano model usage and responses API
- **Practical Example**: Maersk company history generation
- **Skills Gained**: Latest model integration

#### **Audio Processing** (`lesson_audio.py`)
- **Objective**: Generate and process audio content
- **Key Concepts**:
  - Multimodal API usage (text + audio)
  - Voice selection and audio formats
  - Audio data handling and file output
- **Practical Example**: Text-to-speech with file saving
- **Skills Gained**: Audio content generation

#### **Image Generation** (`lesson_image.py`)
- **Objective**: Create images using AI
- **Key Concepts**:
  - Image generation tool integration
  - Base64 image handling
  - File output management
- **Practical Example**: Container ship at Mumbai port visualization
- **Skills Gained**: Visual content creation

#### **Advanced Reasoning** (`lesson_reasoning.py`)
- **Objective**: Leverage enhanced reasoning capabilities
- **Key Concepts**:
  - Reasoning effort configuration
  - Complex problem-solving workflows
  - Multi-criteria decision analysis
- **Practical Example**: Port operations planning with cost-benefit analysis
- **Skills Gained**: Decision support systems

#### **Comprehensive Tool Use** (`lesson_tool_use.py`)
- **Objective**: Master all available OpenAI tools
- **Key Concepts**:
  - Web search integration
  - Code interpreter usage
  - File search and vector stores
  - Image generation workflows
  - Tool orchestration
- **Supported Tools**:
  - `web_search_preview` - Real-time web information
  - `code_interpreter` - Python code execution
  - `file_search` - Document analysis
  - `image_generation` - Visual content creation
  - `mcp` - Model Context Protocol
  - `computer_use_preview` - System interaction
- **Skills Gained**: Multi-tool AI applications

## 🛤️ Learning Path

### **Beginner Track** (Complete Newcomers)
1. **Setup Environment** → Follow setup instructions
2. **Module 1 Foundations** → `lesson0.py` → `lesson1.py` → `Lesson3.py`
3. **Practice Chat Apps** → `chat_demo.py` → `chat_with_memory.py`
4. **Module 2 Functions** → `lesson_structured_output.py` → `lesson_function_calling.py`

### **Intermediate Track** (Basic API Experience)
1. **Review Module 1** → Focus on `lesson1.py` and `Lesson3.py`
2. **Master Module 2** → Both function calling lessons
3. **Explore Module 3** → `lesson_gpt5.py` → `lesson_reasoning.py`

### **Advanced Track** (Experienced Developers)
1. **Module 2 Deep Dive** → Function calling and structured outputs
2. **Module 3 Complete** → All advanced features
3. **Integration Projects** → Combine multiple tools in `lesson_tool_use.py`

### **Recommended Study Order**
```
Week 1: lesson0.py → lesson1.py → chat_demo.py
Week 2: Lesson3.py → lesson_structured_output.py
Week 3: lesson_function_calling.py → chat_with_memory.py
Week 4: lesson_gpt5.py → lesson_reasoning.py
Week 5: lesson_audio.py → lesson_image.py
Week 6: lesson_tool_use.py → Integration projects
```

## 🔍 Key Learning Outcomes

After completing this course, you will be able to:

- **Design effective prompts** using delimiters, structured outputs, and few-shot examples
- **Implement custom function calling** with proper error handling and validation
- **Create chat applications** with conversation memory and context management
- **Generate multimedia content** including audio and images
- **Build complex reasoning workflows** for decision-making applications
- **Integrate multiple AI tools** for comprehensive solutions
- **Apply enterprise-grade practices** for production AI applications

## 🚨 Troubleshooting

### Common Issues & Solutions

**API Key Errors**
```python
# Ensure your .env file is properly configured
OPENAI_API_KEY=sk-proj-your-actual-key-here
```

**Import Errors**
```bash
# Reinstall dependencies
pip install --upgrade openai python-dotenv pydantic
```

**Model Availability**
- GPT-5 models may have limited availability
- Fall back to GPT-4 models if needed
- Check OpenAI status page for service updates

**File Path Issues**
- Use absolute paths for file operations
- Ensure proper directory structure
- Check file permissions for output operations

## 📖 Additional Resources

### Official Documentation
- [OpenAI API Reference](https://platform.openai.com/docs/api-reference)
- [Function Calling Guide](https://platform.openai.com/docs/guides/function-calling)
- [Prompt Engineering Guide](https://platform.openai.com/docs/guides/prompt-engineering)

### Community Resources
- [OpenAI Community Forum](https://community.openai.com/)
- [OpenAI Cookbook](https://github.com/openai/openai-cookbook)

### Best Practices
1. **Start Simple**: Begin with basic prompts before adding complexity
2. **Iterate Frequently**: Refine prompts based on outputs
3. **Use Examples**: Few-shot prompting significantly improves results
4. **Structure Outputs**: JSON format enables easier processing
5. **Handle Errors**: Implement proper error handling for production use
6. **Monitor Usage**: Track API usage and costs
7. **Security First**: Never expose API keys in code or version control

---

## 🎓 Course Completion

Upon completing all modules, you'll have comprehensive knowledge of:
- Professional prompt engineering
- Custom function integration
- Multimedia AI applications
- Advanced reasoning systems
- Production-ready AI implementations

**Next Steps**: Consider exploring enterprise applications, building custom tools, or contributing to the OpenAI community.

---

*Happy Learning! 🚀*

**Course Maintainer**: [Farhan Khan]
**Last Updated**: October 2025
**Version**: 1.0 (Maersk Edition)
