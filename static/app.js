async function loadPortfolio() {
    try {
        const response = await fetch('/api/all');
        const data = await response.json();

        // Profile
        document.getElementById('name').textContent = data.profile.name;
        document.getElementById('title').textContent = data.profile.title;
        document.getElementById('bio').textContent = data.profile.bio;

        // Education
        const edu = data.education;
        document.getElementById('education').innerHTML = `
            <h3 style="margin-bottom: 10px;">${edu.institution}</h3>
            <p><strong>Спеціальність:</strong> ${edu.specialization}</p>
            <p><strong>Період:</strong> ${edu.period}</p>
            <p><strong>Статус:</strong> ${edu.status}</p>
        `;

        // Hard Skills
        const hardSkillsHTML = data.hard_skills.map(skill => `
            <div class="skill-card">
                <div class="skill-name">${skill.name}</div>
                <div><strong>Рівень:</strong> ${skill.level}</div>
                <div><strong>Досвід:</strong> ${skill.experience}</div>
            </div>
        `).join('');
        document.getElementById('hard-skills').innerHTML = hardSkillsHTML;

        // Soft Skills
        const softSkillsHTML = data.soft_skills.map(skill => `
            <div class="soft-skill-item">${skill}</div>
        `).join('');
        document.getElementById('soft-skills').innerHTML = softSkillsHTML;

        // Projects
        const projectsHTML = data.projects.map(project => `
            <div class="project-card">
                <div class="project-title">${project.title}</div>
                <p>${project.description}</p>
                <div class="tech-tags">
                    ${project.technologies.map(tech =>
                        `<span class="tech-tag">${tech}</span>`
                    ).join('')}
                </div>
            </div>
        `).join('');
        document.getElementById('projects').innerHTML = projectsHTML;

        // Contact
        const contactHTML = `
            <div class="contact-item">
                <h3>📱 Телефон</h3>
                <a href="tel:${data.contact.phone}">${data.contact.phone}</a>
            </div>
            <div class="contact-item">
                <h3>✉️ Email</h3>
                <a href="mailto:${data.contact.email}">${data.contact.email}</a>
            </div>
            <div class="contact-item">
                <h3>💼 GitHub</h3>
                <a href="${data.contact.github}" target="_blank">Переглянути профіль</a>
            </div>
            <div class="contact-item">
                <h3>🔗 LinkedIn</h3>
                <a href="${data.contact.linkedin}" target="_blank">Переглянути профіль</a>
            </div>
        `;
        document.getElementById('contact').innerHTML = contactHTML;

        // Show content
        document.getElementById('loading').style.display = 'none';
        document.getElementById('content').style.display = 'block';
    } catch (error) {
        console.error('Error loading portfolio:', error);
        document.getElementById('loading').textContent = 'Помилка завантаження. Спробуйте оновити сторінку.';
    }
}

// Load portfolio when page is ready
loadPortfolio();