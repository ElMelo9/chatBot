# Define los patrones y respuestas
patrones = [
    #Saludo inicial
    (r'(hola|hi|hey|¡Hola!|¡Hola|¡Hey|¡Hi)', ['¡Hola! 👋 Bienvenido a Namekusein, tu lugar para eventos especiales. ¿Con quién tenemos el gusto de hablar? 😊🎉']),
    (r'(bienvenido|welcome)', ['¡Bienvenido! 👋 Namekusein es el lugar perfecto para tus eventos especiales. ¿Cómo podemos ayudarte hoy? 😊🎉']),
    (r'(saludos|hello)', ['¡Saludos! 👋 Bienvenido a Namekusein, donde tus eventos se vuelven realidad. ¿En qué podemos asistirte? 😊🎉']),
    (r'(inicio|comenzar)', ['¡Hola! 👋 Estás a punto de comenzar una experiencia única en Namekusein, tu lugar para eventos especiales. ¿En qué podemos ayudarte hoy? 😊🎉']),
    (r'(quiero informacion|necesito ayuda)', ['¡Claro! Estamos aquí para proporcionarte información y asistencia. ¿En qué podemos ayudarte hoy en Namekusein? 😊🎉']),
    (r'(listo para empezar|vamos a comenzar)', ['¡Perfecto! Vamos a comenzar. Namekusein es tu destino para eventos especiales. ¿Cómo podemos ayudarte hoy? 😊🎉']),
    (r'(hey there|hey|saludos a todos)', ['¡Hey! 👋 Namekusein está aquí para hacer tus eventos especiales aún más especiales. ¿En qué podemos ayudarte hoy? 😊🎉']),
    (r'(hola equipo|hola Namekusein)', ['¡Hola! 👋 El equipo de Namekusein te da la bienvenida. ¿En qué podemos asistirte? 😊🎉']),
    (r'(que tal|como estas|que hay de nuevo)', ['¡Hola! 👋 Estamos listos para ayudarte en Namekusein, tu lugar para eventos especiales. ¿En qué podemos servirte hoy? 😊🎉']),
    (r'(buenos días|buenas tardes|buenas noches)', ['¡Buenos días/tardes/noches! 👋 Namekusein está disponible en cualquier momento para tus necesidades de eventos especiales. ¿En qué podemos ayudarte? 😊🎉']),
    (r'(hola, soy nuevo aqui)', ['¡Hola, nuevo amigo! 👋 Namekusein te da la bienvenida. ¿En qué podemos ayudarte en tu primer visita? 😊🎉']),
    (r'(saludos desde (.*))', ['¡Saludos desde {tu ubicación}! 👋 Bienvenido a Namekusein. ¿En qué podemos ayudarte hoy? 😊🎉']),
      #servicios
      (r'(servicios|cuales son tus servicios|que servicios ofrecen|servicios disponibles)', ['Ofrecemos una amplia gama de servicios para hacer que tu evento sea especial. ¿En qué tipo de evento estás interesado? 😊🎉']),
      (r'(que tipos de eventos atienden|eventos que pueden organizar|eventos posibles)', ['Atendemos diversos tipos de eventos, desde bodas hasta conferencias. ¿Tienes un evento en mente? Cuéntanos más. 😊🎉']),
      (r'(necesito información sobre los servicios|quiero saber más sobre los servicios|detalles de los servicios)', ['Claro, estamos aquí para proporcionarte información detallada sobre nuestros servicios. ¿En qué específicamente estás interesado? 😊🎉']),
      (r'(qué ofrecen|ofertas disponibles|qué tienes para eventos)', ['Tenemos muchas ofertas emocionantes para tus eventos. ¿Qué tipo de evento estás planeando? 😊🎉']),
      (r'(pueden organizar [nombre de evento]|ofrecen [nombre de evento]|qué opciones hay para [nombre de evento])', ['Sí, podemos organizar [nombre de evento]. Cuéntanos más sobre tus necesidades específicas. 😊🎉']),
      (r'(explícame los servicios|información sobre tus servicios|servicios de Namekusein)', ['Estamos encantados de explicarte nuestros servicios. ¿En qué aspecto necesitas más información? 😊🎉']),
      #descripcion servicios
      (r'(cumpleaños|fiestas de cumpleaños|celebración de cumpleaños)', ['En las fiestas de cumpleaños, creamos un ambiente divertido y lleno de sorpresas para celebrar ese día especial. Cuéntanos más sobre tu idea y te diremos cómo podemos hacerlo único. 😊🎂🎉']),
      (r'(celebracion|fiesta|fiestas|eventos de fiesta|celebraciones divertidas)', ['Las fiestas son nuestra especialidad. Desde temáticas únicas hasta entretenimiento emocionante, estamos aquí para hacer que tu fiesta sea inolvidable. ¿En qué podemos ayudarte con tu fiesta? 😊🎉']),
      (r'(grados|graduaciones|ceremonias de grado)', ['En las ceremonias de grado, creamos un ambiente académico y festivo para celebrar tus logros. ¿Qué tipo de graduación estás planeando? Cuéntanos y te diremos cómo hacerlo especial. 😊🎓🎉']),
      (r'(matrimonio|boda|bodas|matrimonios|ceremonias de boda)', ['Las bodas son momentos mágicos. Ofrecemos todo, desde ceremonias íntimas hasta bodas de gran escala. ¿Tienes una visión para tu boda? Cuéntanos y haremos que se haga realidad. 😊💍🎉']),
      (r'(reuniones|eventos de reunión|encuentros corporativos)', ['En las reuniones, nos aseguramos de que cada detalle esté cuidado. ¿Tienes una reunión en mente? Cuéntanos más y te proporcionaremos soluciones personalizadas. 😊👥🎉']),
      #precios
      (r'(costo|precio|tarifa) (cumpleaño|cumpleaños|fiesta|fiestas|grado|grados|boda|bodas|reunion|reuniones)', ['El costo de nuestros servicios para {2} varía según tus necesidades específicas. Por favor, dinos más sobre tu evento y te proporcionaremos una cotización personalizada. 😊']),
      (r'(cuánto cuesta|precio de) (cumpleaño|cumpleaños|fiesta|fiestas|grado|grados|boda|bodas|reunion|reuniones)', ['El precio de {2} depende de varios factores. Cuéntanos más sobre tu evento y te daremos una estimación de costos. 😊']),
      (r'(me puedes decir el precio para|cotización para) (cumpleaño|cumpleaños|fiesta|fiestas|grado|grados|boda|bodas|reunion|reuniones)', ['Por supuesto, estaríamos encantados de proporcionarte una cotización para {2}. ¿Puedes proporcionarnos más detalles sobre tu evento? 😊']),
      (r'(precio aproximado|costo promedio) (cumpleaño|cumpleaños|fiesta|fiestas|grado|grados|boda|bodas|reunion|reuniones)', ['El precio aproximado para {2} varía según tus preferencias y necesidades. ¿Puedes compartir más información sobre tu evento? 😊']),
      (r'(costo de los servicios|tarifas para eventos|cuánto debo pagar) (cumpleaño|cumpleaños|fiesta|fiestas|grado|grados|boda|bodas|reunion|reuniones)', ['Las tarifas para {2} son personalizadas. ¿Podrías decirnos más sobre lo que tienes en mente para tu evento? 😊']),
      #reservar
      (r'(reservar|cómo reservar|cómo puedo hacer una reserva|quiero hacer una reserva)', ['¡Genial! Estamos aquí para ayudarte a hacer una reserva. Por favor, indícanos el tipo de evento y la fecha que tienes en mente para comenzar el proceso de reserva. 😊📅']),
      (r'(reserva de|quiero reservar|cómo agendar) (cumpleaño|cumpleaños|fiesta|fiestas|grado|grados|boda|bodas|reunion|reuniones)', ['Puedes reservar {2} con nosotros. Por favor, proporciona más detalles sobre tu evento, como la fecha y el número de invitados, para que podamos ayudarte con la reserva. 😊']),
      (r'(disponibilidad de fecha|fechas disponibles para|puedo reservar para) (cumpleaño|cumpleaños|fiesta|fiestas|grado|grados|boda|bodas|reunion|reuniones)', ['Claro, podemos verificar la disponibilidad de fechas para tu evento. Por favor, dime la fecha deseada y te diremos si está disponible. 😊📅']),
      (r'(reservar espacio|agendar fecha) para (cumpleaño|cumpleaños|fiesta|fiestas|grado|grados|boda|bodas|reunion|reuniones)', ['Estás en el lugar correcto para reservar espacio para tu {2}. Cuéntanos más sobre tu evento y te ayudaremos a agendar la fecha. 😊📆']),
      (r'(cuándo puedo reservar|cómo funciona la reserva) (cumpleaño|cumpleaños|fiesta|fiestas|grado|grados|boda|bodas|reunion|reuniones)', ['El proceso de reserva para {2} es sencillo. Por favor, dime más sobre tus preferencias y te proporcionaremos más detalles sobre cómo funciona. 😊']),
      # Consultas sobre ubicación
      (r'(donde estan ubicados|ubicación del salon|dirección de Namekusein)', 
      ['Nos encontramos en [Dirección]. ¿Necesitas más detalles o direcciones para llegar? 😊🗺️', 
      'Nuestra ubicación es [Dirección]. Si requieres indicaciones específicas, por favor avísanos. 😊🏢']),

      (r'(horario de atencion|cuándo están abiertos|horas de operacion)',
      ['Nuestro horario de atención es [Horario]. ¿En qué más podemos ayudarte? 😊⏰',
      'Estamos abiertos de [Horario]. ¿Hay algo más en lo que te podamos asistir? 😊⌛']),

      # Preguntas sobre capacidad
      (r'(cuantas personas pueden acomodar|capacidad del salon|tamaño del espacio)',
      ['Nuestro espacio puede acomodar a [Número de Personas] personas cómodamente. ¿Tienes un estimado de invitados para tu evento? 😊👥',
      'La capacidad de nuestro salón es de aproximadamente [Número de Personas] personas. ¿Cuántos invitados esperas en tu evento? 😊🎉']),

      # Consultas sobre catering
      (r'(ofrecen servicio de catering|pueden proporcionar comida|opciones de comida)',
      ['Sí, ofrecemos servicio de catering para eventos. ¿Tienes alguna preferencia en particular o algún tipo de comida en mente? 😊🍽️',
       'Claro, proporcionamos servicio de catering. ¿Tienes alguna preferencia culinaria que te gustaría discutir? 😊🥘']),

      (r'(menu de catering|opciones de comida|platos disponibles)',
      ['Nuestro menú de catering incluye una variedad de opciones deliciosas. ¿Quisieras ver el menú o tienes alguna preferencia en mente? 😊🍲',
      'Tenemos un menú de catering con una amplia selección de platos. ¿Tienes alguna preferencia alimentaria que debamos tener en cuenta? 😊🍽️']),

      # Preguntas sobre personalización
      (r'(personalizacion|personalizar evento|temáticas de eventos)',
       ['Nos especializamos en personalizar eventos según tus preferencias. ¿Tienes alguna idea en mente que te gustaría incorporar en tu evento? 😊🎨',
      'Estamos aquí para personalizar tu evento y hacerlo único. ¿Tienes alguna temática o detalle especial que desees agregar? 😊🎉']),

      # Consultas sobre disponibilidad
      (r'(disponibilidad de eventos|fechas disponibles para eventos|puedo reservar para [mes])',
      ['Verificar la disponibilidad de fechas para eventos es importante. ¿Tienes un mes específico en mente? 😊📅',
      'Claro, podemos verificar la disponibilidad de fechas para tu evento. ¿Puedes proporcionarnos más información sobre la fecha deseada? 😊🗓️']),

      # Preguntas generales sobre el proceso de reserva
      (r'(como funciona la reserva|proceso de reserva|pasos para reservar)',
      ['El proceso de reserva es sencillo. Por favor, cuéntanos más sobre tu evento y te guiaremos a través de los pasos. 😊📆',
      'Te ayudaremos a comprender el proceso de reserva paso a paso. ¿En qué tipo de evento estás interesado en reservar? 😊🗂️']),

      (r'(cuanto tiempo de antelación|cuando debo reservar)',
      ['Recomendamos reservar con [Cantidad de Tiempo] de antelación para garantizar la disponibilidad. ¿Cuándo tienes planeado tu evento? 😊⏳',
      'La antelación en la reserva es importante. ¿Tienes una fecha específica en mente para tu evento? 😊📅']),

      # Preguntas sobre paquetes y promociones
      (r'(paquetes de eventos|promociones especiales|ofertas disponibles)',
      ['Tenemos paquetes especiales y promociones para eventos. ¿Te gustaría conocer más detalles sobre nuestras ofertas actuales? 😊💼',
      'Nuestros paquetes de eventos pueden ahorrarte dinero. ¿Quisieras conocer más sobre las promociones vigentes? 😊🎁']),

      # Consultas sobre redes sociales
      (r'(redes sociales de Namekusein|cuentas de redes sociales)',
      ['Puedes seguirnos en nuestras redes sociales para obtener actualizaciones y novedades. Nuestras cuentas son [Redes Sociales]. 😊📱',
      '¡Síguenos en las redes sociales para mantenerte al tanto de nuestras últimas noticias y eventos! 😊👍']),

      # Consulta sobre contacto
      (r'(contacto|cómo comunicarse con ustedes|número de telefono)',
      ['Puedes contactarnos en el número [Número de Teléfono] o a través de nuestro correo electrónico [Correo Electrónico]. ¿En qué más podemos ayudarte? 😊📞',
      'Estamos disponibles para contactarnos por teléfono al [Número de Teléfono] o por correo electrónico a [Correo Electrónico]. ¿En qué podemos asistirte']),

      (r'bye|hasta luego', ['¡Hasta luego!', 'Adiós. ¡Vuelve pronto!', 'Nos vemos.'])
   # Agrega más patrones aquí
]