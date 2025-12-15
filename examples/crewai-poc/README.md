# CrewAI Proof of Concept - IEEEZC Agent Crew

This is a sample CrewAI implementation demonstrating multi-agent collaboration for the Pulse Platform.

## Overview

This POC showcases how multiple AI agents can work together to accomplish complex tasks, serving as a reference implementation for the Pulse Multi-Agent Platform.

## Files

- `main.py` - Main entry point and crew orchestration
- `executor_agent.py` - Agent responsible for task execution

## Requirements

```bash
pip install crewai python-dotenv
```

## Usage

1. Create a `.env` file with your configuration
2. Run the crew:
   ```bash
   python main.py
   ```

## Note

This is a proof-of-concept implementation. For production use, refer to the main backend implementation in `/backend`.
