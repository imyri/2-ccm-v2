
| Tools(python_scripts) | **Core Function**                                                                    | **Frequency** | **Tech Stack**                 |
| --------------------- | ------------------------------------------------------------------------------------ | ------------- | ------------------------------ |
| **TrendTracer**       | `/trendtracer`: Scans YouTube/Twitter for trending brand topics.                     | Daily         | `Serper.dev` / `BeautifulSoup` |
| **ScriptSmith**       | `/scriptsmith`: Generates omnichannel scripts (YouTube, IG, Twitter, FB).            | Daily         | **Claude Sonnet 4.6**          |
| **MotionMuse**        | `/motionmuse`: Assembles video assets, images, gif, voiceovers, and dynamic mockups. | Daily         | `MoviePy` / `HeyGen API`       |
| **EchoBlast**         | `/echoblast`: Posts to all socials and manages the **Linktree**.                     | Daily         | `Meta Graph API` / `Selenium`  |
| **NexusNode**         | `/nexusnode`: Automates community engagement and **Gumroad** delivery.               | Real-time     | `Skool API` / `Webhook`        |
| **RevenueReaper**     | `/revenuereaper`: Syncs **Stripe** sales and **YouTube Ad-sense** to HDFC.           | Daily         | `Stripe SDK` / `Pandas`        |
| **BountyBroker**      | `/bountybroker`: Identifies high-commission SaaS and digital tools.                  | Weekly        | `Scrapy` / `ProductHunt API`   |
| **SpecSpy**           | `/specspy`: Deep-dives into tool features for high-authority reviews.                | Weekly        | **Claude Opus 4.6**            |
| **HookHammer**        | `/hookhammer`: Crafts comparison and tutorial-style scripts.                         | Weekly        | **Claude Sonnet 4.6**          |
| **PixelPilot**        | `/pixelplpt`: Monitors affiliate link conversions and click-through rates.           | Daily         | `Impact.com` / `PartnerStack`  |
| **LedgerLord**        | `/ledgerlord`: Verifies affiliate payouts and directs them to HDFC.                  | Weekly        | `Python` / `Gmail API`         |



# **CCM — AI-Powered Content Creation Machine**

The **CCM** is a modular automation platform for indie creators built on the **I.A.M.** architecture and a **Folder-as-Workspace** routing system. It transforms a standard file system into an autonomous production house that handles everything from trend discovery to final social media distribution.

---

## **1. Core Architecture: I.A.M.**

The system operates on three distinct layers to ensure that AI orchestration is flexible while technical execution remains deterministic and reliable.

- **Instructions (I)**: These are the "brains" of the machine, consisting of Markdown SOPs (Standard Operating Procedures) and localized `CONTEXT.md` files. They define the logic, personas (e.g., high-retention writer), and rules for every workspace.
    
- **Agents (A)**: The intelligence layer (powered by Claude 4.6). Agents read the **Instructions**, navigate the functional workspaces, and orchestrate execution by calling the appropriate **Modules**.
    
- **Modules (M)**: The "muscles" of the system—deterministic Python scripts that perform specific technical tasks like API calls, web scraping, and video assembly.
    

---

## **2. Project Structure (Unified Root & Vault)**

The project root is a unified **Obsidian Vault** organized into "Context Rooms." This structure isolates information so that when an **Agent** is performing a task, it only focuses on relevant data, maximizing token efficiency and output quality.

Plaintext

```
ccm/ 
├── CCM_MAP.md               # [Instructions] Master floor plan & command routing 
├── CLAUDE.md                # [Instructions] Global agent behavior guidelines 
├── config.json              # [Instructions] System settings & API keys 
│
├── 00-System/               # [I.A.M. Core] 
│   ├── instructions/        # All Markdown SOPs 
│   └── modules/             # All Python Skills 
│
├── 01-Discovery/            # [Context Room] Trend Intel & Research 
│   ├── CONTEXT_INTEL.md     # [Instructions] Local vetting rules 
│   ├── Trends/              # [Modules] Data from /trendtracer 
│   └── Research/            # [Agents] Reports from /specspy 
│
├── 02-Narrative/            # [Context Room] Ideation & Scripting 
│   ├── CONTEXT_WRITER.md    # [Instructions] Persona & hook formulas 
│   ├── Ideas/               # [Agents] Angles from /scriptsmith ideation 
│   └── Scripts/             # [Agents] Final drafts from /scriptsmith 
│
├── 03-Production/           # [Context Room] Multimedia Generation 
│   ├── CONTEXT_PRODUCER.md  # [Instructions] Visual & design rules 
│   └── Output/clips/        # [Modules] Assets from /motionmuse 
│
├── 04-Monetization/         # [Context Room] AssetAlpha Products 
│   ├── CONTEXT_MONEY.md     # [Instructions] Product & course standards 
│   ├── Sales/               # [Agents] Specs created for /nexusnode 
│   └── Courses/             # [Agents] Curricula designed for /nexusnode 
│
├── 05-Affiliate/            # [Context Room] LinkLoomer Engine 
│   ├── CONTEXT_PARTNER.md   # [Instructions] Scouting & comparison rules 
│   └── Affiliate/           # [Modules] Research & conversion data 
│
└── 06-Finance/              # [Context Room] Revenue & Payouts 
    ├── Finance/             # [Modules] Sales and reconciliation data 
    └── hdfc_reaper.csv      # [Modules] Processed data for HDFC bank imports 
```

---

## **3. Tech Stack**

The machine is built using a mix of modern AI models and robust Python libraries:

- **Intelligence**: Claude 4.6 (Sonnet and Opus).
    
- **Automation**: free resources and ways to do so `n8n` (Workflow automation) and `Postiz` (Social media scheduling).
    
- **Video & Audio**: Remonition - for Video generation), `MoviePy` (Asset assembly), You suggest free resources and ways to do so
    
- **Data & Scraping**:  free resources and ways to do so like `Serper.dev`, `BeautifulSoup`, `Scrapy`, and `yt-dlp`.
    
- **Business & Finance**: free resources and ways to do so `Stripe SDK`, `Gumroad API`, and `Pandas` (for financial reconciliation).
    
- **Infrastructure**: free resources and ways to do so `Docker` (for self-hosting), `Ngrok` (for Colab tunneling), and `Obsidian` (as the UI).
    

---

## **4. The Execution Flow: Start to End**

#### **Step 1: Signal Intelligence (`/trendtracer`)**

The process begins with the **TrendTracer** module scanning YouTube and Twitter for viral signals in your niche. These are saved as raw signals in the **Discovery** workspace.

#### **Step 2: Deep Analysis (`/specspy`)**

The **SpecSpy** agent enters the room, reads the raw signals, and performs deep-dive research to create a structured, factual report.

#### #**Step 3: Creative Ideation & Scripting (`/scriptsmith`)**

Based on the research, the **ScriptSmith** agent generates and ranks content ideas, then writes a high-retention script optimized for multiple social platforms.

#### **Step 4: Asset Fabrication (`/motionmuse`)**

The **MotionMuse** module takes the script and its production blueprint to assemble B-roll assets, voiceovers, and dynamic mockups.

#### **Step 5: Platform Launch (`/echoblast`)**

Finally, the **EchoBlast** module publishes the finished content across all socials and manages the associated link ecosystem.

---


## **5. Quick Setup & Module Commands**

1. **Install Modules**: `pip install yt-dlp snscrape requests anthropic stripe playwright pandas`.
    
2. **Set Environment**: Populate your `.env` with your `ANTHROPIC_API_KEY`.
    
3. **Run Modules**: Use the slash commands directly in your Agent chat (e.g., `/trendtracer "Forex"`).
    

|**Command**|**Module**|**Focus Area**|
|---|---|---|
|**`/trendtracer`**|**TrendTracer**|Trend Discovery|
|**`/specspy`**|**SpecSpy**|Deep Research|
|**`/scriptsmith`**|**ScriptSmith**|Writing & Ideation|
|**`/motionmuse`**|**MotionMuse**|Video Assembly|
|**`/echoblast`**|**EchoBlast**|Platform Launch|
|**`/nexusnode`**|**NexusNode**|Community & Delivery|
|**`/bountybroker`**|**BountyBroker**|Affiliate Scouting|
|**`/revenuereaper`**|**RevenueReaper**|Financial Sync|
