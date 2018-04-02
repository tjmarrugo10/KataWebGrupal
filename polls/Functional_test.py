import random
import sys

import os

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

        self.browser.find_element_by_xpath("//select[@id='id_tiposDeServicio']/option[text()='Desarrollador Web']").click()
        telefono = self.browser.find_element_by_id('id_telefono')
        telefono.send_keys('3166875247')

        correo = self.browser.find_element_by_id('id_correo')
        correo.send_keys('ca.mendoza968@uniandes.edu.co')

        imagen = self.browser.find_element_by_id('id_imagen')
        ruta= os.path.join(sys.path[0], "polls/files", 'image.jpg')
        imagen.send_keys(ruta)

        nombreUsuario = self.browser.find_element_by_id('id_username')
        nombreUsuario.send_keys('ca.mendoza968')

        clave = self.browser.find_element_by_id('id_password')
        clave.send_keys('clave123')

        botonGrabar = self.browser.find_element_by_id('id_grabar')
        botonGrabar.click()
        self.browser.implicitly_wait(3)
        span=self.browser.find_element(By.XPATH, '//span[text()="Camilo Mendoza"]')

        self.assertIn('Camilo Mendoza', span.text)


    def test_verDetalle(self):
        self.browser.get('http://localhost:8000')
        span=self.browser.find_element(By.XPATH, '//span[text()="Camilo Mendoza"]')
        span.click()

        h2=self.browser.find_element(By.XPATH, '//h2[text()="Camilo Mendoza"]')

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