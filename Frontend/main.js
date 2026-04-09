/**
 * CCM V2 - Interactive Frontend Controller
 * Handles modal logic, terminal simulation, and machine animations.
 */

document.addEventListener('DOMContentLoaded', () => {
    initTerminal();
    initModals();
    initScrollAnimations();
});

/**
 * High-Fidelity Terminal Simulation
 */
function initTerminal() {
    const feed = document.getElementById('terminal-feed');
    const logs = [
        { text: "SCANNING_VECTORS: [YOUTUBE_API]", type: "normal" },
        { text: "TRIGGER_FOUND: 'AI_AUTOMATION_2026'", type: "success" },
        { text: "DISPATCHING_SPEC_SPY_PROBES...", type: "normal" },
        { text: "EXTRACTING_TRANSCRIPTS...", type: "processing" },
        { text: "INJECTING_CONTEXT_INTO_GEMINI_MODEL...", type: "processing" },
        { text: "REPORT_COMPILED: technical_audit_01.md", type: "success" },
        { text: "SCRIPT_SMITH_ORCHESTRATION_STARTED", type: "normal" },
        { text: "GENERATING_HOOK_VARIANTS...", type: "processing" },
        { text: "MOTION_MUSE_ASSET_SYNC_COMPLETE", type: "success" },
        { text: "PUSHING_TO_AIRTABLE_MASTER...", type: "normal" },
        { text: "ECOSYSTEM_SYNC_LOCKED", type: "sync" }
    ];

    let index = 0;

    function addLog() {
        const log = logs[index];
        const line = document.createElement('div');
        line.className = `log-line ${log.type}`;
        line.innerHTML = `<span class="cmd">></span> ${log.text}`;
        
        feed.appendChild(line);
        feed.scrollTop = feed.scrollHeight;

        index = (index + 1) % logs.length;
        
        // Random interval for realism
        setTimeout(addLog, 2000 + Math.random() * 3000);
    }

    // Start after initial delay
    setTimeout(addLog, 3000);
}

/**
 * Modal System for Machine Nodes
 */
function initModals() {
    const rooms = document.querySelectorAll('.node-room');
    
    rooms.forEach(room => {
        room.addEventListener('click', () => {
            const roomId = room.id;
            const roomName = room.querySelector('h3').innerText;
            const roomData = getRoomDetails(roomId);
            
            showModal(roomName, roomData);
        });
    });
}

function getRoomDetails(id) {
    const data = {
        'room-discovery': {
            icon: '🔍',
            tagline: 'The Eyes of the Machine',
            desc: 'TrendTracer automates the discovery of high-velocity topics by analyzing engagement patterns across X, YouTube, and specialized RSS feeds.',
            tech: ['YouTube Data API v3', 'X (Twitter) Pro API', 'Custom Scrapers'],
            output: 'Viral Trigger Objects'
        },
        'room-research': {
            icon: '🧠',
            tagline: 'Synthetic Intelligence',
            desc: 'SpecSpy acts as the research arm, using Gemini 1.5 Flash to perform deep technical audits and competitive analysis on discovered trends.',
            tech: ['Google GenAI SDK', 'Gemini 1.5 Flash', 'Technical Spec Extraction'],
            output: 'Markdown Research Reports'
        },
        'room-narrative': {
            icon: '✍️',
            tagline: 'Creative Fabrication',
            desc: 'ScriptSmith and MotionMuse transform raw data into cinematic scripts and precise shot lists, optimized for retention and authority.',
            tech: ['LLM Creative Templates', 'MotionMuse Shot Engine', 'Visual Branding Logic'],
            output: 'Production-Ready Scripts'
        },
        'room-sync': {
            icon: '⚡',
            tagline: 'Platform Propagation',
            desc: 'The final stage pushes all generated assets to the Airtable Master Base and initializes ecosystem sync across content platforms.',
            tech: ['Airtable API', 'Webhooks', 'Cloudinary (Asset Hosting)'],
            output: 'Synced Project Entries'
        }
    };
    return data[id] || {};
}

function showModal(title, details) {
    // Create modal if it doesn't exist
    let modal = document.getElementById('machine-modal');
    if (!modal) {
        modal = document.createElement('div');
        modal.id = 'machine-modal';
        modal.className = 'modal-overlay';
        modal.innerHTML = `
            <div class="modal-content glass">
                <button class="close-modal">&times;</button>
                <div class="modal-body"></div>
            </div>
        `;
        document.body.appendChild(modal);
        
        modal.querySelector('.close-modal').onclick = () => {
            modal.classList.remove('active');
        };
        
        window.onclick = (event) => {
            if (event.target == modal) {
                modal.classList.remove('active');
            }
        };
    }
    
    const body = modal.querySelector('.modal-body');
    body.innerHTML = `
        <div class="modal-header">
            <span class="modal-icon">${details.icon}</span>
            <div class="modal-title-group">
                <h2>${title}</h2>
                <span class="modal-tagline">${details.tagline}</span>
            </div>
        </div>
        <div class="modal-description">
            <p>${details.desc}</p>
        </div>
        <div class="modal-grid">
            <div class="modal-info-card">
                <h4>Core Tech</h4>
                <ul>${details.tech.map(t => `<li>${t}</li>`).join('')}</ul>
            </div>
            <div class="modal-info-card">
                <h4>Output Artifact</h4>
                <div class="output-badge">${details.output}</div>
            </div>
        </div>
    `;
    
    modal.classList.add('active');
}

/**
 * Scroll Animations
 */
function initScrollAnimations() {
    const observerOptions = {
        threshold: 0.1
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('in-view');
            }
        });
    }, observerOptions);

    document.querySelectorAll('.node-room, .hero-content, .signals-container').forEach(el => {
        observer.observe(el);
    });
}
