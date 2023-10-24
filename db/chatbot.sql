-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 05-09-2023 a las 22:57:50
-- Versión del servidor: 10.4.24-MariaDB
-- Versión de PHP: 8.0.19

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `chatbot`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `historialchat`
--

CREATE TABLE `historialchat` (
  `id_historialChat` int(11) NOT NULL,
  `id_usuario` int(11) NOT NULL,
  `fecha_historialChat` date NOT NULL,
  `chat_usuario` text NOT NULL,
  `estado_usuario` binary(1) NOT NULL DEFAULT '1',
  `FechaReg` datetime NOT NULL DEFAULT current_timestamp(),
  `FechaMod` datetime NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `historialchat`
--

INSERT INTO `historialchat` (`id_historialChat`, `id_usuario`, `fecha_historialChat`, `chat_usuario`, `estado_usuario`, `FechaReg`, `FechaMod`) VALUES
(25, 33, '2023-09-05', 'Eder Melo Gonzalez: hola----------', 0x31, '2023-09-05 15:34:09', '2023-09-05 15:34:09'),
(26, 33, '2023-09-05', 'Dende: ¡Hola!  Bienvenido a Namekusein, tu lugar para eventos especiales. ¿Con quién tenemos el gusto de hablar? ----------', 0x31, '2023-09-05 15:34:09', '2023-09-05 15:34:09'),
(27, 33, '2023-09-05', 'Eder Melo Gonzalez: como estas----------', 0x31, '2023-09-05 15:34:09', '2023-09-05 15:34:09'),
(28, 33, '2023-09-05', 'Dende: ¡Hola!  Estamos listos para ayudarte en Namekusein, tu lugar para eventos especiales. ¿En qué podemos servirte hoy? ----------', 0x31, '2023-09-05 15:34:09', '2023-09-05 15:34:09'),
(29, 33, '2023-09-05', 'Eder Melo Gonzalez: cuales son los servicios----------', 0x31, '2023-09-05 15:34:09', '2023-09-05 15:34:09'),
(30, 33, '2023-09-05', 'Dende: Ofrecemos una amplia gama de servicios para hacer que tu evento sea especial. ¿En qué tipo de evento estás interesado? ----------', 0x31, '2023-09-05 15:34:09', '2023-09-05 15:34:09'),
(31, 33, '2023-09-05', 'Eder Melo Gonzalez: una boda----------', 0x31, '2023-09-05 15:34:09', '2023-09-05 15:34:09'),
(32, 33, '2023-09-05', 'Dende: Las bodas son momentos mágicos. Ofrecemos todo, desde ceremonias íntimas hasta bodas de gran escala. ¿Tienes una visión para tu boda? Cuéntanos y haremos que se haga realidad. ----------', 0x31, '2023-09-05 15:34:09', '2023-09-05 15:34:09'),
(33, 33, '2023-09-05', 'Eder Melo Gonzalez: donde estan ubicados----------', 0x31, '2023-09-05 15:34:09', '2023-09-05 15:34:09'),
(34, 33, '2023-09-05', 'Dende: Nuestra ubicación es [Dirección]. Si requieres indicaciones específicas, por favor avísanos. ----------', 0x31, '2023-09-05 15:34:09', '2023-09-05 15:34:09'),
(35, 33, '2023-09-05', 'Eder Melo Gonzalez: gracias quisiera reservar----------', 0x31, '2023-09-05 15:34:09', '2023-09-05 15:34:09'),
(36, 33, '2023-09-05', 'Dende: ¡Genial! Estamos aquí para ayudarte a hacer una reserva. Por favor, indícanos el tipo de evento y la fecha que tienes en mente para comenzar el proceso de reserva. ----------', 0x31, '2023-09-05 15:34:09', '2023-09-05 15:34:09'),
(37, 33, '2023-09-05', 'Eder Melo Gonzalez: adios----------', 0x31, '2023-09-05 15:34:09', '2023-09-05 15:34:09'),
(38, 33, '2023-09-05', 'Dende: ----------', 0x31, '2023-09-05 15:34:09', '2023-09-05 15:34:09'),
(39, 34, '2023-09-05', 'Yuris Medina Padilla: hola----------', 0x31, '2023-09-05 15:47:04', '2023-09-05 15:47:04'),
(40, 34, '2023-09-05', 'Dende: ¡Hola!  Bienvenido a Namekusein, tu lugar para eventos especiales. ¿Con quién tenemos el gusto de hablar? ----------', 0x31, '2023-09-05 15:47:04', '2023-09-05 15:47:04'),
(41, 34, '2023-09-05', 'Yuris Medina Padilla: gracias cuales son sus servicios----------', 0x31, '2023-09-05 15:47:04', '2023-09-05 15:47:04'),
(42, 34, '2023-09-05', 'Dende: Ofrecemos una amplia gama de servicios para hacer que tu evento sea especial. ¿En qué tipo de evento estás interesado? ----------', 0x31, '2023-09-05 15:47:04', '2023-09-05 15:47:04'),
(43, 34, '2023-09-05', 'Yuris Medina Padilla: un cumpleaños----------', 0x31, '2023-09-05 15:47:04', '2023-09-05 15:47:04'),
(44, 34, '2023-09-05', 'Dende: En las fiestas de cumpleaños, creamos un ambiente divertido y lleno de sorpresas para celebrar ese día especial. Cuéntanos más sobre tu idea y te diremos cómo podemos hacerlo único. ----------', 0x31, '2023-09-05 15:47:04', '2023-09-05 15:47:04'),
(45, 34, '2023-09-05', 'Yuris Medina Padilla: donde estan ubicados----------', 0x31, '2023-09-05 15:47:04', '2023-09-05 15:47:04'),
(46, 34, '2023-09-05', 'Dende: Nuestra ubicación es [Dirección]. Si requieres indicaciones específicas, por favor avísanos. ----------', 0x31, '2023-09-05 15:47:04', '2023-09-05 15:47:04'),
(47, 34, '2023-09-05', 'Yuris Medina Padilla: precio de cumpleaños----------', 0x31, '2023-09-05 15:47:04', '2023-09-05 15:47:04'),
(48, 34, '2023-09-05', 'Dende: El precio de {2} depende de varios factores. Cuéntanos más sobre tu evento y te daremos una estimación de costos. ----------', 0x31, '2023-09-05 15:47:04', '2023-09-05 15:47:04'),
(49, 34, '2023-09-05', 'Yuris Medina Padilla: quiero reservar el lugar----------', 0x31, '2023-09-05 15:47:04', '2023-09-05 15:47:04'),
(50, 34, '2023-09-05', 'Dende: ¡Genial! Estamos aquí para ayudarte a hacer una reserva. Por favor, indícanos el tipo de evento y la fecha que tienes en mente para comenzar el proceso de reserva. ----------', 0x31, '2023-09-05 15:47:04', '2023-09-05 15:47:04'),
(51, 34, '2023-09-05', 'Yuris Medina Padilla: gracias adios----------', 0x31, '2023-09-05 15:47:04', '2023-09-05 15:47:04'),
(52, 34, '2023-09-05', 'Dende: ----------', 0x31, '2023-09-05 15:47:04', '2023-09-05 15:47:04'),
(53, 34, '2023-09-05', 'Yuris Medina Padilla: adios----------', 0x31, '2023-09-05 15:47:04', '2023-09-05 15:47:04'),
(54, 34, '2023-09-05', 'Dende: ----------', 0x31, '2023-09-05 15:47:04', '2023-09-05 15:47:04');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tipo_documento`
--

CREATE TABLE `tipo_documento` (
  `id_tipoDoc` int(11) NOT NULL,
  `tipoDoc` varchar(2) NOT NULL,
  `descripcion_tipoDoc` varchar(30) NOT NULL,
  `estado_tipoDoc` binary(1) DEFAULT '1'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `tipo_documento`
--

INSERT INTO `tipo_documento` (`id_tipoDoc`, `tipoDoc`, `descripcion_tipoDoc`, `estado_tipoDoc`) VALUES
(1, 'TI', 'Tarjeta de identidad', 0x31),
(2, 'CC', 'Cedula de ciudadania', 0x31),
(3, 'CE', 'Cedula de extranjeria', 0x31),
(4, 'PS', 'Pasaporte', 0x31),
(5, 'PT', 'Permiso temporal', 0x31),
(6, 'PE', 'Permiso especial', 0x31);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `id_usuario` int(11) NOT NULL,
  `id_tipoDoc` int(11) NOT NULL,
  `doc_usuario` int(20) NOT NULL,
  `nombre_usuario` varchar(100) NOT NULL,
  `email_usuario` varchar(50) NOT NULL,
  `telefono_usuario` varchar(20) NOT NULL,
  `estado_usuario` binary(1) NOT NULL DEFAULT '1',
  `FechaReg` datetime NOT NULL DEFAULT current_timestamp(),
  `FechaMod` datetime NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`id_usuario`, `id_tipoDoc`, `doc_usuario`, `nombre_usuario`, `email_usuario`, `telefono_usuario`, `estado_usuario`, `FechaReg`, `FechaMod`) VALUES
(33, 1, 1047343259, 'Eder Melo Gonzalez', 'efmelo9@gmail.com', '3003422755', 0x31, '2023-09-05 15:32:45', '2023-09-05 15:32:45'),
(34, 2, 1001785986, 'Yuris Medina Padilla', 'efmelo9@gmail.com', '3002878166', 0x31, '2023-09-05 15:44:45', '2023-09-05 15:44:45');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `historialchat`
--
ALTER TABLE `historialchat`
  ADD PRIMARY KEY (`id_historialChat`),
  ADD KEY `id_usuario` (`id_usuario`);

--
-- Indices de la tabla `tipo_documento`
--
ALTER TABLE `tipo_documento`
  ADD PRIMARY KEY (`id_tipoDoc`);

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`id_usuario`),
  ADD UNIQUE KEY `doc_usuario` (`doc_usuario`),
  ADD KEY `id_tipoDoc` (`id_tipoDoc`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `historialchat`
--
ALTER TABLE `historialchat`
  MODIFY `id_historialChat` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=55;

--
-- AUTO_INCREMENT de la tabla `tipo_documento`
--
ALTER TABLE `tipo_documento`
  MODIFY `id_tipoDoc` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `id_usuario` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=35;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `historialchat`
--
ALTER TABLE `historialchat`
  ADD CONSTRAINT `historialchat_ibfk_1` FOREIGN KEY (`id_usuario`) REFERENCES `usuarios` (`id_usuario`);

--
-- Filtros para la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD CONSTRAINT `usuarios_ibfk_1` FOREIGN KEY (`id_tipoDoc`) REFERENCES `tipo_documento` (`id_tipoDoc`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
