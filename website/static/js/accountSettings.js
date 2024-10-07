function toggles() {
    var blur = document.getElementById('mainContent');
    if (blur) {
        blur.classList.toggle('active');
    }
    var popup = document.getElementById('settingsCont');
    popup.classList.toggle('actived');
}
