def iniciar_sesion (usuario, contraseña):
    usuario_correcto = "admin"
    contraseña_correcta = "password"
    
    try:
    # validar usuario y contraseña 
        if usuario != usuario_correcto:
            raise ValueError("nombre de usuario incorrecto")
        elif contraseña != contraseña_correcta:
            raise ValueError ("contraseña incorrecta")
        else:
            print("inicio de sesion exitoso")
            
    except ValueError as e:
        print (f"error: {e}")
        
# ejemplo de uso 
# deberia inicir sesion correctamente
iniciar_sesion("admin, password") 
# deberia mostrar un mensaje de error 
iniciar_sesion("usuario incorrecto","password")