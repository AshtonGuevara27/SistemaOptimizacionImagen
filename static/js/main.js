function validarFormulario() {
    const nombre = document.getElementById('nombre').value;
    const correo = document.getElementById('correo').value;
    const imagen = document.getElementById('imagen').files[0];

    // El nombre no puede estar vacio
    if (nombre === '') {
        alert('Por favor escribe tu nombre.');
        return false;
    }

    // El correo debe tener una @
    if (correo.indexOf('@') === -1) {
        alert('Por favor escribe un correo valido.');
        return false;
    }

    // Debe haber una imagen seleccionada
    if (!imagen) {
        alert('Por favor selecciona una imagen.');
        return false;
    }

    // Si todo esta bien, se envia el formulario
    return true;
}