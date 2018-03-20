import requests
from bs4 import BeautifulSoup as BS
from twilio.rest import Client
from twilio.twiml.messaging_response import Body, Message, Redirect, MessagingResponse
from flask import Flask, Response, request
import time
import random
import proxy

# Twilio #
account_sid = "AC4f13fe4df35eba9f9e572316976f2e6d"
auth_token = "3f62cb3660465b4f3cdbfa5182d51307"
client = Client(account_sid, auth_token)
# Twilio END #

###################### 		Data Update 			###################################

def update():
	while 1:
		def check():
			prox = {'http': proxy.main()}
			www = 'https://offerup.com/search/?q=iphone#offers'
			r = requests.get(www, proxies=prox)
			soup = BS(r.content, 'lxml')
			item = soup.find_all('div', {'class' : 'item-pic'})
			item_price = soup.find_all('span', {'class' : 'size-large-xx color-gray-darker medium'})
			urls = []
			sell_average = ''
		
			for x in item:
				url = x.find_all('a')
				for y in url:
					urls.append(y.get('href'))
					
			return urls[0]


		
		new_url = check()
	
		time.sleep(random.randint(1,15))
	
		if new_url != check():
			print('new update!')
		else:
			www = new_url
			r = requests.get(www, proxies=prox)
			soup = BS(r.content, 'lxml')
			item_price = soup.find_all('span', {'class' : 'size-large-xx color-gray-darker medium'})
			item_desc = soup.find_all('div', {'class' : 'left base-size medium color-gray-darker'})
			item_desc2 = soup.find_all('div', {'class' : 'pad-more'})

			for z in item_desc:
				item_title = z.find_all('h1')
				item_loc = z.find_all('a', {'class' : 'color-gray-darker'})
				item_time = z.find_all('div', {'class' : 'pad-less-top color-text'})

				for titl in item_title:
					titl = titl.text

				for location in item_loc:
					loc = location.text	

				for ti in item_time:
					tim = ti.text	

				for des in item_desc2:
					desc = des.text

			tim = tim.replace('  ', '')
			

			for price in item_price:
				price2 = price.text

			for z in item_desc:
				title = z.find_all('h1')
				for t in title:
					print(t.text)
##### Price Check #######
					www = 'http://www.thepricegeek.com/results/' + t.text + '?country=us'
					r = requests.get(www, proxies=prox)
					soup = BS(r.content, 'lxml')
					item = soup.find_all('em', {'class' : 'median'})
					for mean in item:
						price = mean.text.replace('$', '')
						price = float(price)
						if price > price2:
							client.api.account.messages.create(
			    				to="+17866832638",
			    				from_="+18333946893",
			    				body="Less the average sell price" + '\n' +'Title - ' + str(titl) + '\n' + "Price - " + str(price) + "\n" + "Sell average - " + str(price2) + "\n" + "Location - " + str(loc) + '\n' + "Description - "  )

						else:
							print("not too good")	
								
		##### Price Check END ######

###################### 		Data Update  END		###################################

######################		GET OFFERUP DATA		###################################
def main():
	prox = {'http': proxy.main()}
	www = 'https://offerup.com/search/?q=iphone#offers'
	r = requests.get(www)
	soup = BS(r.content, 'lxml')
	item = soup.find_all('div', {'class' : 'item-pic'})
	
	item_url = []
	for x in item:
		a = x.find_all('a')
		for y in a:
			print('Current iphone listing: ' + y.get('href'))
			www = y.get('href')
			r = requests.get(www)
			soup = BS(r.content, 'lxml')
			item_price = soup.find_all('span', {'class' : 'size-large-xx color-gray-darker medium'})
			item_desc = soup.find_all('div', {'class' : 'left base-size medium color-gray-darker'})
			item_img = soup.find_all('li', {'class' : 'flex-active-slide'})
			item_desc2 = soup.find_all('div', {'class' : 'pad-more'})
	
			item_dict = {'url' : '', 'price' : '', 'location' : '', 'title' : '', 'post_time' : '', 'item_desc' : '', 'sell_average' : ''}
	
			item_dict['url'] = y.get('href')
	
			for z in item_price:
				print('Current listing price $: ' + z.text)
				item_dict['price'] = z.text
	
				for z in item_desc:
					item_title = z.find_all('h1')
					item_loc = z.find_all('a', {'class' : 'color-gray-darker'})
					item_time = z.find_all('div', {'class' : 'pad-less-top color-text'})
	
				for item in item_loc:
					print('Current listing location: ' + item.text)
					item_dict['location'] = item.text
	
				for title in item_title:
					print('Current listing title: ' + title.text)
					item_dict['title'] = title.text
					www = 'http://www.thepricegeek.com/results/' + title.text + '?country=us'
					r = requests.get(www)
					soup = BS(r.content, 'lxml')
					item = soup.find_all('em', {'class' : 'median'})
					for mean in item:
						print("Current listing selling price: " + mean.text.replace('  ', ''))
						item_dict['sell_average'] = mean.text.replace('  ', '')

##### Price Check ######
					www = 'http://www.thepricegeek.com/results/' + title.text + '?country=us'
					r = requests.get(www)
					soup = BS(r.content, 'lxml')
					item = soup.find_all('span', {'class' : 'complavgprice'})
					for mean in item:
						print("Current listing selling price: " + mean.text.replace('  ', ''))
						item_dict['sell_average'] = mean.text.replace('  ', '')
##### Price Check ######	
	
				for time in item_time:
					print("Current listing post time: "	+ time.text.replace('  ', ''))
					item_dict['post_time'] = time.text.replace('  ', '')
	
	
			for z in item_desc2:
				item_description = z.find_all('div', {"class" : 'pad-less-top-bottom'})
				for desc in item_description:
					print("Current item description: " + desc.text + "\n" + "\n")
					item_dict['item_desc'] = desc.text
	
	######################		GET OFFERUP DATA END	###################################
	
	########### STAR CONFIG #########
	
		it = item_dict['sell_average'].replace('$','')
		if item_dict['sell_average'] != '':
			one_star = float(it) - (float(it) * .1)
			two_star = float(it) - (float(it) * .2)
			three_star = float(it) - (float(it) * .3)
			four_star = float(it) - (float(it) * .4)
			five_star = float(it) - (float(it) * .5)
			nine_star = float(it) - (float(it) * .9)
	
		else:
			pass	
	#
		#if( item_dict['sell_average'] == '' ):
		#	pass
	#
		#elif( float(item_dict['price'].replace(',','')) < float(item_dict['sell_average'].replace('$', '').replace(',','')) ): #float(item_dict['sell_average'].replace('$', ''))):
		#	print 'less then sell average price'
		#	client.api.account.messages.create(
		#	    to="+17866832638",
		#	    from_="+18333946893",
		#	    body="Less the average sell price" + '\n' +'Title - ' + item_dict['title'] + '\n' + "Price - " + item_dict['price'] + '\n' + 'Selling Price - ' + item_dict['sell_average'] +  '\n' + 'Post Time - ' + item_dict['post_time'] + '\n' + 'Location - ' + item_dict['location'] + '\n' + 'Description - ' +  item_dict['item_desc'] + '\n' + 'Url - ' + item_dict['url'])
		#else:
		#	pass

		return str(item_dict)

	########### STAR CONFIG END #####

if __name__ == '__main__':
	main()
	update()




