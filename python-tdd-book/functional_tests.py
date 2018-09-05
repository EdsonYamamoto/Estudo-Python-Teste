
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

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest
class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        #check home page
        self.browser.get('http://localhost:8000')

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
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        #self.assertTrue(
        #    any(row.text == '1: Buy peacock feathers' for row in rows),
        #    f"New to-do item did not appear in table. Contents were:\n{table.text}"  
        #)
        self.assertIn('1: Buy peacock feathers', [row.text for row in rows])
        #self.fail('Finish test!')

if __name__ == '__main__':  
    unittest.main(warnings='ignore') 
