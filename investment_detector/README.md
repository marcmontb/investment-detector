# Investment Detector

An automated system for detecting and analyzing investment-related emails using Microsoft Graph API, Mistral AI, and Airtable.

## Features

- Automatically fetch emails using Microsoft Graph API
- Analyze emails for investment-related content
- Generate summaries using Mistral AI
- Store results in Airtable
- Customizable processing pipelines

## Prerequisites

- Python 3.8 or higher
- Microsoft 365 account with Graph API access
- Airtable account
- Mistral AI API access

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/investment-detector.git
   cd investment-detector
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:
   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - Unix/MacOS:
     ```bash
     source venv/bin/activate
     ```

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Copy `.env.example` to `.env`:
   ```bash
   cp .env.example .env
   ```

6. Configure your environment variables in `.env`

## Configuration

Set up the following environment variables in your `.env` file:

- `MSGRAPH_CLIENT_ID`: Your Microsoft Graph API client ID
- `MSGRAPH_CLIENT_SECRET`: Your Microsoft Graph API client secret
- `MSGRAPH_TENANT_ID`: Your Microsoft tenant ID
- `AIRTABLE_API_KEY`: Your Airtable API key
- `AIRTABLE_BASE_ID`: Your Airtable base ID
- `AIRTABLE_TABLE_NAME`: Your Airtable table name
- `MISTRAL_API_KEY`: Your Mistral AI API key

## Usage

1. Process emails using the default pipeline:
   ```python
   from investment_detector.pipelines.email_processor import EmailProcessor

   processor = EmailProcessor()
   await processor.process_emails()
   ```

2. Create a custom pipeline:
   ```python
   from investment_detector.pipelines.custom_pipelines import Pipeline
   from investment_detector.core.analyzer import EmailAnalyzer
   from investment_detector.core.summarizer import EmailSummarizer

   pipeline = Pipeline()
   pipeline.add_step(EmailAnalyzer().analyze_email)
   pipeline.add_step(EmailSummarizer().summarize)
   ```

## Testing

Run the test suite:
```bash
pytest
```

Run