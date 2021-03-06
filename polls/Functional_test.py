import os
import sys

__author__ = 'asistente'
from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By


class FunctionalTest(TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(executable_path=r"files/chromedriver.exe")
        self.browser.implicitly_wait(2)

    def tearDown(self):
        self.browser.quit()

    def test_title(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('Busco Ayuda', self.browser.title)

    def test_registro(self):
        self.browser.get('http://localhost:8000')
        link = self.browser.find_element_by_id('id_register')
        link.click()

        nombre = self.browser.find_element_by_id('id_nombre')
        nombre.send_keys('Camilo')

        apellidos = self.browser.find_element_by_id('id_apellidos')
        apellidos.send_keys('Mendoza')

        experiencia = self.browser.find_element_by_id('id_aniosExperiencia')
        experiencia.send_keys('5')

        self.browser.find_element_by_xpath(
            "//select[@id='id_tiposDeServicio']/option[text()='Desarrollador Web']").click()
        telefono = self.browser.find_element_by_id('id_telefono')
        telefono.send_keys('3166875247')

        correo = self.browser.find_element_by_id('id_correo')
        correo.send_keys('ca.mendoza968@uniandes.edu.co')

        imagen = self.browser.find_element_by_id('id_imagen')
        ruta = os.path.join(sys.path[0], "polls/files", 'image.jpg')
        imagen.send_keys(ruta)

        nombreUsuario = self.browser.find_element_by_id('id_username')
        nombreUsuario.send_keys('ca.mendoza968')

        clave = self.browser.find_element_by_id('id_password')
        clave.send_keys('clave123')

        botonGrabar = self.browser.find_element_by_id('id_grabar')
        botonGrabar.click()
        self.browser.implicitly_wait(3)
        span = self.browser.find_element(By.XPATH, '//span[text()="Camilo Mendoza"]')

        self.assertIn('Camilo Mendoza', span.text)

    def test_verDetalle(self):
        self.browser.get('http://localhost:8000')
        span = self.browser.find_element(By.XPATH, '//span[text()="Camilo Mendoza"]')
        span.click()

        h2 = self.browser.find_element(By.XPATH, '//h2[text()="Camilo Mendoza"]')

        self.assertIn('Camilo Mendoza', h2.text)

    def test_login(self):
        self.browser.get('http://localhost:8000')
        link = self.browser.find_element_by_id('id_login')
        link.click()
        nombreUsuario = self.browser.find_element_by_id('id_username')
        nombreUsuario.send_keys('ca.mendoza968')

        clave = self.browser.find_element_by_id('id_password')
        clave.send_keys('clave123')

        botonIniciar = self.browser.find_element_by_id('id_login_')
        botonIniciar.click()
        self.browser.implicitly_wait(3)
        span = self.browser.find_element(By.XPATH, '/html/body/ul/li[2]/a')

        self.assertIn('Logout', span.text)

    def test_editar(self):
        self.browser.get('http://localhost:8000')
        link = self.browser.find_element_by_id('id_login')
        link.click()
        nombreUsuario = self.browser.find_element_by_id('id_username')
        nombreUsuario.send_keys('ca.mendoza968')

        clave = self.browser.find_element_by_id('id_password')
        clave.send_keys('clave123')

        botonIniciar = self.browser.find_element_by_id('id_login_')
        botonIniciar.click()
        self.browser.implicitly_wait(3)
        self.browser.find_element_by_css_selector('body > div.alert.alert-success.success.float-message > a').click()

        botonEditar = self.browser.find_element_by_id('id_editar')
        botonEditar.click()
        self.browser.implicitly_wait(3)

        nombre = self.browser.find_element_by_id('id_nombre')
        nombre.clear()
        nombre.send_keys('Taidy')

        apellidos = self.browser.find_element_by_id('id_apellidos')
        apellidos.clear()
        apellidos.send_keys('Marrugo')

        experiencia = self.browser.find_element_by_id('id_aniosExperiencia')
        experiencia.clear()
        experiencia.send_keys('10')

        telefono = self.browser.find_element_by_id('id_telefono')
        telefono.clear()
        telefono.send_keys('123456')

        correo = self.browser.find_element_by_id('id_correo')
        correo.clear()
        correo.send_keys('taidy@uniandes.edu.co')

        imagen = self.browser.find_element_by_id('id_imagen')
        ruta = os.path.join(sys.path[0], "polls/files", 'image.jpg')
        imagen.send_keys(ruta)

        self.browser.find_element_by_id('id_editar_').click()
        self.browser.implicitly_wait(3)

        botonEditar = self.browser.find_element_by_id('id_editar')
        botonEditar.click()
        self.browser.implicitly_wait(3)

        nombre_2 = self.browser.find_element_by_id('id_nombre')
        self.assertIn("Taidy", nombre_2.get_attribute("value"))

        apellidos_2 = self.browser.find_element_by_id('id_apellidos')
        self.assertIn("Marrugo", apellidos_2.get_attribute("value"))


    def test_comentario(self):
        self.browser.get('http://localhost:8000')
        link = self.browser.find_element_by_css_selector('#trabajadores > div:nth-child(1) > div > div.panel-body > a > span')
        link.click()
        correo = self.browser.find_element_by_id('correo')
        correo.send_keys('ca.mendoza968@uniandes.edu.co')

        comentario = self.browser.find_element_by_id('comentario')
        comentario.send_keys('hola mundo')

        botonEnviar = self.browser.find_element_by_css_selector('body > div:nth-child(2) > div > form > button')
        botonEnviar.click()
        self.browser.implicitly_wait(3)
        span = self.browser.find_element(By.XPATH, '//h4[text()="ca.mendoza968@uniandes.edu.co"]')
        self.assertIn('ca.mendoza968@uniandes.edu.co', span.text)

        span_ = self.browser.find_element(By.XPATH, '//p[text()="hola mundo"]')
        self.assertIn('hola mundo', span_.text)
