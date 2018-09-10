
    #novo aplicativo online chamado To-Do, verifica a nova pagina

    #Existe o nome 'To-Do' na pagina

    #receber o invite para entrar no APP de modo unico

    #Ela escreve "Buy peacock feathers" numa text box 'robby do usuario'

    #Quando apertar enter, da um update da pagina, e agora lista da pagina posssui o item "1:buy peacock feathers" como item  da lista de to-do

    #Então deve existir uma caixa de texto para convidar a adicionar outro item. ela escreve "use peacock feather to make a fly" o usuario é muito metódico

    #a pagina deve dar update novamente, e agora os 2 itens devem ser mostrados

    # o usuario se perguntar se o site vai conter as informações ao relogar na pagina

    #o site deverá ter uma URL unica

    # ela visita aquela URL e verifica que seus itens ainda estão salvos

    #satisfeita ela volta a dormir

from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest
from selenium.common.exceptions import WebDriverException

MAX_WAIT=10

class NewVisitorTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        time.sleep(3)
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        #check home page
        self.browser.get(self.live_server_url)

        self.assertIn('To-Do', self.browser.title)

        header_text = self.browser.find_element_by_tag_name('h1').text
        #self.fail('finish the test!')

        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        #<input id="id_new_item" placeholder="Enter a to-do item" />
        #<table id="id_list_table">
        #</table>
        #</body>
 
        inputbox.send_keys('Buy peacock feathers')
        inputbox.send_keys(Keys.ENTER)
        
        self.wait_for_row_in_in_list_table('1: Buy peacock feathers')
        #self.fail('Finish test!')

        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)

        self.wait_for_row_in_in_list_table('1: Buy peacock feathers')
        self.wait_for_row_in_in_list_table('2: Use peacock feathers to make a fly')

    def wait_for_row_in_in_list_table(self, row_text):
        start_time = time.time()
        while True:
            try:
                table =self.browser.find_element_by_id('id_list_table')
                rows = table.find_elements_by_tag_name('tr')
                self.assertIn(row_text, [row_text for row in rows])
                return
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time>MAX_WAIT:
                    raise e
                time.sleep(0.5)