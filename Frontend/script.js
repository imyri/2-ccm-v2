// CCM V2.0 Control Logic
let currentStatus = 'Idle';
let lastLogCount = 0;
const views = ['dashboard', 'discovery', 'narrative', 'production'];

// DOM Elements
const nicheInput = document.getElementById('nicheInput');
const automateBtn = document.getElementById('automateBtn');
const progressBar = document.getElementById('progressBar');
const progressPercent = document.getElementById('progressPercent');
const currentStepText = document.getElementById('currentStepText');
const globalStatus = document.getElementById('globalStatus');
const terminal = document.getElementById('terminal');

/**
 * Switch between defined views
 */
function switchView(viewId) {
    // Update Sidebar
    document.querySelectorAll('.nav-item').forEach(item => {
        item.classList.remove('active');
        if (item.getAttribute('onclick')?.includes(viewId)) {
            item.classList.add('active');
        }
    });

    // Update Content
    views.forEach(v => {
        const el = document.getElementById(v);
        if (el) {
            if (v === viewId) {
                el.classList.add('active');
            } else {
                el.classList.remove('active');
            }
        }
    });

    // Refresh assets if entering an asset view
    if (viewId !== 'dashboard') {
        loadAssets();
    }
}

/**
 * Trigger Automation
 */
async function startAutomation() {
    const niche = nicheInput.value.trim();
    if (!niche) return alert('Please enter a target niche.');

    try {
        const res = await fetch('/automate', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ niche })
        });
        
        if (res.ok) {
            terminal.innerHTML = '<div class="log-entry"><span>[SYS]</span> Initializing autonomous loop...</div>';
            lastLogCount = 0;
            updateDashboard();
        }
    } catch (e) {
        console.error('Automation Start Error:', e);
    }
}

/**
 * Update Dashboard State & Vitals
 */
async function updateDashboard() {
    try {
        const res = await fetch('/status');
        const data = await res.json();
        
        // Status Updates
        currentStatus = data.status;
        globalStatus.textContent = data.status;
        globalStatus.style.color = data.status === 'Running' ? 'var(--accent-primary)' : 
                                   data.status === 'Completed' ? 'var(--success)' : 
                                   data.status === 'Waiting for Approval' ? '#ff9800' :
                                   data.status === 'Error' ? 'var(--error)' : 'var(--text-dim)';
        
        currentStepText.textContent = data.current_step || 'Awaiting Input...';
        
        // Progress
        const prog = data.progress || 0;
        progressBar.style.width = `${prog}%`;
        progressPercent.textContent = `${prog}%`;

        // Stepper Update
        updateStepper(prog, data.status);

        // Button State
        automateBtn.disabled = data.status === 'Running' || data.status === 'Waiting for Approval';
        if (data.status === 'Running') {
            automateBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> RUNNING...';
        } else if (data.status === 'Waiting for Approval') {
            automateBtn.innerHTML = '<i class="fas fa-pause-circle"></i> AWAITING APPROVAL...';
        } else {
            automateBtn.innerHTML = '<i class="fas fa-bolt-lightning"></i> START PIPELINE';
        }
        
        // Logs
        renderLogs(data.logs);
        
        // If finished, reload vital counts
        if (data.status === 'Completed') {
            loadAssets();
        }
    } catch (e) {
        // Silent fail on polling
    }
}

/**
 * Update the visual process stepper
 */
function updateStepper(progress, status) {
    const nodes = [
        document.getElementById('step-node-1'),
        document.getElementById('step-node-2'),
        document.getElementById('step-node-3'),
        document.getElementById('step-node-4')
    ];

    nodes.forEach(n => n.classList.remove('active', 'complete'));

    if (status === 'Completed') {
        nodes.forEach(n => n.classList.add('complete'));
    } else if (progress > 0) {
        if (progress < 55) {
            nodes[0].classList.add('active');
        } else if (progress < 85) {
            nodes[0].classList.add('complete');
            nodes[1].classList.add('active');
        } else if (progress < 100) {
            nodes[0].classList.add('complete');
            nodes[1].classList.add('complete');
            nodes[2].classList.add('active');
        }
    }
}

/**
 * Render Logs in terminal
 */
function renderLogs(logs) {
    if (!logs || logs.length === lastLogCount) return;
    
    const newLogs = logs.slice(lastLogCount);
    newLogs.forEach(log => {
        const entry = document.createElement('div');
        entry.className = 'log-entry';
        if (log.toLowerCase().includes('error')) entry.classList.add('err');
        if (log.toLowerCase().includes('complete') || log.toLowerCase().includes('success')) entry.classList.add('ok');
        
        const ts = new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit', second: '2-digit' });
        entry.innerHTML = `<span>[${ts}]</span> ${log}`;
        terminal.appendChild(entry);
    });
    
    lastLogCount = logs.length;
    terminal.scrollTop = terminal.scrollHeight;
}

/**
 * Load and Organize Assets into Sub-Grids
 */
async function loadAssets() {
    try {
        const res = await fetch('/assets');
        const assets = await res.json();
        
        // Grids
        const grids = {
            'Trends': document.getElementById('grid-trends'),
            'Signals': document.getElementById('grid-signals'),
            'Sync': document.getElementById('grid-sync'),
            'Research': document.getElementById('grid-research'),
            'Scripts': document.getElementById('grid-scripts'),
            'Assets': document.getElementById('grid-assets'),
            'Shots': document.getElementById('grid-shots')
        };

        // Clear all
        Object.values(grids).forEach(g => { if(g) g.innerHTML = ''; });

        let signalCount = 0;
        let scriptCount = 0;

        assets.forEach(asset => {
            const card = createAssetCard(asset);
            const grid = grids[asset.sub_category];
            if (grid) {
                grid.appendChild(card);
            }

            if (asset.sub_category === 'Signals') signalCount++;
            if (asset.sub_category === 'Scripts') scriptCount++;
        });

        // Update Vitals
        const sigEl = document.getElementById('discoveryCount');
        const scrEl = document.getElementById('scriptsCount');
        if (sigEl) sigEl.textContent = signalCount;
        if (scrEl) scrEl.textContent = scriptCount;

        // Empty states hint
        Object.keys(grids).forEach(key => {
            const g = grids[key];
            if (g && !g.innerHTML) {
                g.innerHTML = `<p style="color:var(--text-dim); font-size:0.9rem; grid-column: 1/-1;">No ${key.toLowerCase()} generated yet.</p>`;
            }
        });

    } catch (e) {
        console.error('Asset Load Error:', e);
    }
}

/**
 * Create Premium Asset Card
 */
function createAssetCard(asset) {
    const date = new Date(asset.date * 1000).toLocaleDateString(undefined, { month: 'short', day: 'numeric', hour: '2-digit', minute: '2-digit' });
    const div = document.createElement('div');
    div.className = 'asset-item';
    
    let icon = 'fa-file-lines';
    if (asset.type === 'Trend') icon = 'fa-arrow-trend-up';
    if (asset.type === 'Signal') icon = 'fa-bolt';
    if (asset.type === 'Sync') icon = 'fa-rotate';
    if (asset.type === 'Research') icon = 'fa-microscope';
    if (asset.type === 'Script') icon = 'fa-scroll';
    if (asset.type === 'Asset') icon = 'fa-photo-film';
    if (asset.type === 'ShotList') icon = 'fa-video';

    div.innerHTML = `
        <div class="asset-meta">
            <span class="asset-badge">${asset.type}</span>
            <span style="font-size: 0.7rem; color: var(--text-dim)">${date}</span>
        </div>
        <div class="asset-name">
            <i class="fas ${icon}" style="margin-right: 10px; color: var(--accent-primary)"></i>
            ${asset.name}
        </div>
        <div class="asset-footer">
            <a href="${asset.path}" target="_blank" class="btn-view">
                <i class="fas fa-external-link-alt"></i> View Raw
            </a>
            <button class="btn-view" style="border:none; background:none; cursor:pointer;" onclick="previewAsset('${asset.path}', '${asset.type}')">
                <i class="fas fa-magnifying-glass"></i> Preview
            </a>
        </div>
    `;
    return div;
}

async function previewAsset(path, type) {
    const overlay = document.getElementById('previewOverlay');
    const content = document.getElementById('previewContent');
    overlay.style.display = 'flex';
    content.innerHTML = '<p class="fa-spin fas fa-spinner"></p> Loading...';

    try {
        const res = await fetch(path);
        const text = await res.text();
        
        if (path.endsWith('.json')) {
            const json = JSON.parse(text);
            if (Array.isArray(json) && json.length > 0) {
                content.innerHTML = renderJsonTable(json);
            } else {
                content.innerHTML = `<pre style="color:var(--accent-secondary)">${JSON.stringify(json, null, 2)}</pre>`;
            }
        } else {
            content.innerHTML = `<div style="white-space: pre-wrap; line-height: 1.6;">${text}</div>`;
        }
    } catch (e) {
        content.innerHTML = 'Error loading preview.';
    }
}

/**
 * Render JSON Array as a Premium Table
 */
function renderJsonTable(data) {
    if (!Array.isArray(data) || data.length === 0) return '';
    
    const keys = Object.keys(data[0]);
    let html = `<table class="premium-table"><thead><tr>`;
    
    // Header
    keys.forEach(key => {
        html += `<th>${key.replace(/_/g, ' ')}</th>`;
    });
    html += `</tr></thead><tbody>`;
    
    // Rows
    data.forEach(row => {
        html += `<tr>`;
        keys.forEach(key => {
            const val = row[key];
            let displayVal = typeof val === 'object' ? JSON.stringify(val) : val;
            
            // Auto-link URLs
            if (typeof displayVal === 'string' && displayVal.startsWith('http')) {
                displayVal = `<a href="${displayVal}" target="_blank">${displayVal}</a>`;
            }
            
            const isLong = String(displayVal).length > 100;
            html += `<td title="${typeof val === 'string' ? val : ''}" class="${isLong ? 'long-text' : ''}">${displayVal || '-'}</td>`;
        });
        html += `</tr>`;
    });
    
    html += `</tbody></table>`;
    return html;
}

function closePreview() {
    document.getElementById('previewOverlay').style.display = 'none';
}

function toggleSettings() {
    alert('Pipeline Config: Running on Gemini 2.0 Flash. Threshold: 50% viral variance.');
}

// Event Listeners
automateBtn.addEventListener('click', startAutomation);

// Initialize
setInterval(updateDashboard, 2000);
loadAssets();
window.switchView = switchView; 
window.previewAsset = previewAsset;
window.closePreview = closePreview;
window.toggleSettings = toggleSettings;

console.log('CCM Premium Control Center Engine Online');
