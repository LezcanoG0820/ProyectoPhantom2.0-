# ProyectoPhantom2.0-

Este es un proyecto utilizando el Framework de Django para desarrollo de entornos y aplicaciones web basadas en python. 

El proyecto está en fase de desarrollo y por el momento NO FUNCIONA COMO QUISIERA

El contexto del proyecto es que debemos desarrollar un "Blog" donde hayan diferentes Guias para poder entender La saga "Persona". Se solicita que este proyecto deba contener los siguientes aspectos:
1. Un sistema de registro y atenticacion de usuarios
   * Los usuarios deben poder registrarse en la pagina, proporcionando como minimo un nombre, correo electronico y constrase;a
   * Los usuarios deben poder iniciar y cerrar sesion
   * Las contrase;as de los usuarios deben estar almacenadas de manera segura
2. Categoria de productos
   * Deben poder crear, editar y eleiminar categorias para los productos
   * Cada categoria debe tener al menos un nombre y una descripcion
   * Los usuarios deben poder ver una lista de todas las categorias disponibles
3. Gestion de productos (Guias en nuestro caso)
   * Deben poder agregar, editar y eliminar productos
   * Cada producto debe tener al menos un nombre, descripcion, precio, imagen y categoria asociada.
   * Al hacer clic en un producto, los usuarios deben ver una pagnia de detalle del producto
4. Seccion de reviews para cada producto
   * Los usuarios registrados deben poder dejar un comentario o review sobre el producto
   * Cada review debe contener un comentario y una puntuacion (por ejemplo de 1 a 5 estrellas)
   * En la pagina de detalles del producto, se deben mostrar las reviews asociadas a ese producto
  
Con respecto a segundo punto del aspecto 3, hemos pensado que a nivel de desarrollo, no tiene mucho sencillo cobrar por un modelo de negocio donde cobremos al usuario por el uso de la guia, sin embargo
pensamos que una forma interesante poder implementar un sistema de compra/venta a la pagina, seria mediante "donaciones" de esta forma, si a los usuarios les gusta mucho el contenido que ofrecemos, 
pueden apoyar a los creadores de la web de manera segura mediante una pagina como PayPal. Para esto se debe implementar el sandbox de PayPal en el codigo. 
   
  
