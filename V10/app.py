from bottle import route, run, request, get, post, template
import pymysql.cursors

@route('/', method='get')
def signUpOrLogin():
    return template('index')

@route('/leynisida', method='post')
def signedin():
	u = request.forms.get('user')
	p = request.forms.get('pass')
	connection = pymysql.connect(host='tsuts.tskoli.is', port=3306, user='1907002160', passwd='mypassword', db='1907002160_verkefni10')
	cur = connection.cursor()
	sql = "SELECT `user`,`pass` FROM `user` WHERE `user` = %s  AND `pass` = %s"
	cur.execute(sql, (u,p))
	acc=cur.fetchone()
	try:
		user=acc[0]
		passw=acc[1]

	except TypeError:
		user=None
		passw=None

	if user != None or passw != None:
		if u==user and p==passw: 
			return template('leynisida.tpl')
	else:
		return "rangt notendanafn og/eða lykilorð"

@route('/result', method='post')
def nyr():
	u = request.forms.get('user')
	p = request.forms.get('pass')
	connection = pymysql.connect(host='tsuts.tskoli.is', port=3306, user='1907002160', passwd='mypassword', db='1907002160_verkefni10')
	cur = connection.cursor()
	sql = "SELECT `user` FROM `user` WHERE `user` LIKE %s"
	cur.execute(sql, u)
	acc = cur.fetchone()
	try:
		user = acc[0]
	except TypeError:
		user=None

	if user==u:
		return "Notendanafn er núþegar til"
	else:
		connection = pymysql.connect(host='tsuts.tskoli.is', port=3306, user='1907002160', passwd='mypassword', db='1907002160_verkefni10')
		cur = connection.cursor()
		cur.execute("INSERT INTO `user` (`user`, `pass`) VALUES (%s, %s)", (u,p))
		connection.commit()
		return 'Notandi skráður'


if __name__ == "__main__":
    run(host='localhost', port=8080, debug=True)