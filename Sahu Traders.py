<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Sahu Traders</title>

<style>
body {
    margin: 0;
    font-family: 'Segoe UI', sans-serif;
    background: #fff0f5;
}

/* APP STYLE HEADER */
header {
    background: #ff69b4;
    color: white;
    padding: 15px;
    text-align: center;
    font-size: 20px;
    position: sticky;
    top: 0;
}

/* NAV (APP STYLE) */
nav {
    display: flex;
    justify-content: space-around;
    background: white;
    position: fixed;
    bottom: 0;
    width: 100%;
    border-top: 1px solid #ccc;
}

nav a {
    padding: 10px;
    text-decoration: none;
    color: #ff69b4;
    font-weight: bold;
}

/* SECTIONS */
section {
    padding: 20px;
    margin-bottom: 60px;
}

.card {
    background: white;
    padding: 15px;
    margin: 10px 0;
    border-radius: 12px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
}

/* BUTTONS */
.btn {
    display: block;
    background: #ff1493;
    color: white;
    text-align: center;
    padding: 12px;
    border-radius: 10px;
    text-decoration: none;
    margin-top: 10px;
}

/* WHATSAPP FLOAT */
.whatsapp {
    position: fixed;
    bottom: 70px;
    right: 15px;
    background: #25D366;
    color: white;
    padding: 15px;
    border-radius: 50%;
    text-decoration: none;
    font-size: 20px;
}

/* MAP */
iframe {
    border-radius: 10px;
}
</style>
</head>

<body>

<header>
    🌸 Sahu Traders
</header>

<section id="home">
    <div class="card">
        <h3>Welcome 👋</h3>
        <p>Your one-stop shop for groceries, cold drinks, ice cream, xerox & more.</p>
    </div>
</section>

<section id="services">
    <div class="card">🛒 Grocery Items</div>
    <div class="card">🍦 Ice Cream</div>
    <div class="card">🥤 Cold Drinks</div>
    <div class="card">📄 Xerox</div>
    <div class="card">📑 Lamination</div>
</section>

<section id="order">
    <div class="card">
        <h3>Order Online 🛒</h3>
        <p>Click below to order directly on WhatsApp</p>

        <a class="btn" href="https://wa.me/917008780186?text=Hello%20Sahu%20Traders,%20I%20want%20to%20order">
            Order on WhatsApp
        </a>
    </div>
</section>

<section id="location">
    <div class="card">
        <h3>📍 Our Location</h3>

        <iframe 
        src="https://maps.google.com/maps?q=Sanaparia%20Odisha&t=&z=15&ie=UTF8&iwloc=&output=embed"
        width="100%" height="250"></iframe>

        <a class="btn" href="https://maps.app.goo.gl/8HZzys14Lzrfa1H46" target="_blank">
            Open in Google Maps
        </a>
    </div>
</section>

<section id="contact">
    <div class="card">
        <h3>Contact 📞</h3>
        <p>Phone: +91 7008780186</p>
        <a class="btn" href="tel:+917008780186">Call Now</a>
    </div>
</section>

<!-- WHATSAPP FLOAT BUTTON -->
<a class="whatsapp" href="https://wa.me/917008780186" target="_blank">💬</a>

<!-- BOTTOM NAV -->
<nav>
    <a href="#home">Home</a>
    <a href="#services">Services</a>
    <a href="#order">Order</a>
    <a href="#location">Map</a>
</nav>

</body>
</html>