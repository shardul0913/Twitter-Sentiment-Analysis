
from BeautifulSoup import BeautifulSoup
import urllib, urllib2

'''This class matches the sting entered by the user in the top 10 bing searches and returns the Rank of all the search
results with a match'''

class search_match:

	''' Search Funtion for getting the results from bing.com of the passed query '''

	def search(self, query):
		address = "http://www.bing.com/search?q=%s" % (urllib.quote_plus(query))

		'''Request the address link with 'query' attached to the string'''

		getRequest = urllib2.Request(address, None, {
			'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:54.0) Gecko/20100101 Firefox/54.0'})

		'''Saving the fetched file by opening it with 'urlopen' property, into a file name - urlfile'''

		urlfile = urllib2.urlopen(getRequest)
		htmlResult = urlfile.read(200000)

		urlfile.close()

		'''Open the saved file as a soup object using beautifulSoup'''

		soup = BeautifulSoup(htmlResult)

		'''Extract only the CSS linked text in the 'soup' object by specifying the 'Span' classname
		 and Filter the other tags by replacing them with their child tag'''

		[s.extract() for s in soup('span')]
		unwantedTags = ['a', 'strong', 'cite']
		for tag in unwantedTags:
			for match in soup.findAll(tag):
				match.replaceWithChildren()

		'''Getting all the text between the tags 'li' and class 'b_algo'''

		results = soup.findAll('li', {"class": "b_algo"})
		# for id, result in enumerate(results):
		#        print "# TITLE: " + str(id + 1) + str(result.find('h2')).replace(" ", " ") + "\n#"
		#        print "# DESCRIPTION: " + str(result.find('p')).replace(" ", " ")
		#       print "# ___________________________________________________________\n#"

		return soup, results

	def match_string(self, search_query, search_pattern, *args):

		'''Getting all the return values of the search funtion
		& Save the user Specified Search_pattern in 'pattern' '''

		soup, results = self.search(search_query)
		pattern = search_pattern
		counter_list = []

		found = 0

		''' 'Ennumerate' allows to iterate through each output line generated in 'results' as a dictionary object
		the 'id' is associated with the each result generated one by one in the results file'''

		for id, result in enumerate(results):

			'''''keyword_file' is a string file. It creates a string of only the heading, description and links in
			 the each search result'''

			keyword_file =  str(id + 1) + str(result.find('h2')).replace("<h2>", " ").replace("</h2>",
																										  " ") + "\n"  \
						   + str(result.find('p')).replace("<p>", " ").replace("</p>", " ") + str(
				result.find('div', {"class": "b_attribution"}))
			print keyword_file

			'''if the string matched the pattern specified by the user then return the id+1
			#id starts from 0, by adding 1 we get the corresponding result number
			#for multiple matches the ids will be appended to the list - counter_list '''
			if pattern in keyword_file:
				found = id + 1
				counter_list.append(found)
			else:
				found = 0

		'''if match list is not 0/(empty in this case) return the list else return 0 '''
		if counter_list is not 0:
			return counter_list
		elif counter_list is 0:
			return 0

'''IF the file is called from here itself then the following code will execute'''

if __name__ == "__main__":

	links = search_match()
	links_return_value = links.match_string("ronaldo","wikipedia")
	if (links_return_value == 0):
		print("not found")
	else:
		print links_return_value
























