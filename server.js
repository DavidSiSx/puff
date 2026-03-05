const express = require('express');
const path = require('path');
const app = express();

app.use(express.json());

// Servir la carpeta public para la vista web
app.use(express.static(path.join(__dirname, 'public')));

// ---------------------------------------------------------
// VULNERABILIDAD 1: Filtro de User-Agent ingenuo (Para demostrar Spoofing de Bots)
// ---------------------------------------------------------
app.use((req, res, next) => {
    const userAgent = req.get('User-Agent') || '';
    const blockedAgents = ['python-requests', 'httpx', 'curl'];
    
    const isBlocked = blockedAgents.some(bot => userAgent.toLowerCase().includes(bot));

    if (isBlocked) {
        console.log(`[BLOQUEADO] Intento de bot detectado con User-Agent: ${userAgent}`);
        return res.status(403).json({ error: 'Acceso denegado: Bot detectado' });
    }

    next();
});

// ---------------------------------------------------------
// VULNERABILIDAD 2 y 3: Sin Rate Limit y Authentication Bypass por Header
// ---------------------------------------------------------
app.post('/api/login', (req, res) => {
    const { email, password } = req.body;
    const userAgent = req.get('User-Agent') || '';

    // EL CHISMOSO: Imprime en consola exactamente qué tarjeta de presentación está recibiendo
    console.log("-> Intento de login. User-Agent recibido:", userAgent);

    // VULNERABILIDAD 3: Si detecta la firma del dispositivo del Admin, entra sin contraseña.
    // Usamos .includes() para evitar problemas con espacios invisibles.
    if (userAgent.includes('Pokelab-Admin-Secret-Device')) {
        return setTimeout(() => {
            res.status(200).json({ 
                success: '⚠️ ¡ACCESO CRÍTICO CONCEDIDO! Bienvenido, Administrador Supremo.' 
            });
        }, 50);
    }

    // Flujo normal de login (VULNERABILIDAD 2: El setTimeout simula la base de datos sin Rate Limit)
    if (email === 'trainer@pokelab.gg' && password === 'pikachu123') {
        setTimeout(() => {
            res.status(200).json({ success: 'Login exitoso. Bienvenido, Entrenador.' });
        }, 50);
    } else {
        setTimeout(() => {
            res.status(401).json({ error: 'Credenciales incorrectas' });
        }, 50);
    }
});

// ---------------------------------------------------------
// ENCENDIDO DEL SERVIDOR
// ---------------------------------------------------------

// Ruta para el dashboard
app.get('/dashboard', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'dashboard.html'));
});
const PORT = 3001;
app.listen(PORT, () => {
    console.log(`🚀 Pokelab Mock Server corriendo en http://localhost:${PORT}`);
    console.log(`👁️  Interfaz visual lista en: http://localhost:${PORT}`);
    console.log(`🛡️  API de Login lista en: POST http://localhost:${PORT}/api/login`);
    console.log(`------------------------------------------------------`);
    console.log(`Esperando conexiones...`);
});