from flask import Flask, render_template, redirect, request
from mongodb import col_player, col_record
from player import app_player

app = Flask(__name__)
# app.debug = True

app.register_blueprint(app_player)


@app.route('/display/<time>')#通过rule的get请求传递参数，作为mongodb中pk日志查询条件
def display(time):
    p1 = col_player.find_one({'UserName': 'Player1'})
    p2 = col_player.find_one({'UserName': 'Player2'})

    pk_log = col_record.find_one({'time': time})
    if not pk_log:
        pk_log = {}
    return render_template('display.html', player1=p1, player2=p2, log=pk_log)


if __name__ == '__main__':
    app.run()
