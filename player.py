import random
import time

from flask import Blueprint, request, redirect,jsonify
from mongodb import col_player,col_record

app_player = Blueprint('player', __name__)


@app_player.route('/player/<name>', methods=['POST'])
def player(name):
    username = name

    formdata = request.form

    down_equip = formdata.get('down_equip')
    up_equip = formdata.get('up_equip')

    player_info = col_player.find_one({'UserName': username})

    if up_equip:
        player_package = player_info.get('Package')
        # print(type(player_package),player_package)
        # [{'name': '黄金甲', 'atc': -5, 'def': 20, 'life': 200}, {'name': '98K', 'atc': 20, 'def': -5, 'life': 0}, {'name': '饮料', 'atc': 5, 'def': 0, 'life': 100}]

        for equip in player_package:

            if equip['name'] == up_equip:
                print(equip)  # {'name': '98K', 'atc': 20, 'def': -5, 'life': 0}

                new_info = {
                    'ATC': player_info.get('ATC') + equip.get('atc'),
                    'DEF': player_info.get('DEF') + equip.get('def'),
                    'LIFE': player_info.get('LIFE') + equip.get('life'),
                }
                print(new_info)
                try:
                    col_player.update_one({'UserName': username}, {'$set': new_info})
                    col_player.update_one({'UserName': username}, {'$push': {'Equip': equip}})
                    col_player.update_one({'UserName': username}, {'$pull': {'Package': equip}})

                except:
                    print('装备使用出现错误！')

                break
    if down_equip:
        player_package = player_info.get('Equip')
        for equip in player_package:
            if equip['name'] == down_equip:
                # print(equip)#{'name': '98K', 'atc': 20, 'def': -5, 'life': 0}
                new_info = {
                    'ATC': player_info.get('ATC') - equip.get('atc'),
                    'DEF': player_info.get('DEF') - equip.get('def'),
                    'LIFE': player_info.get('LIFE') - equip.get('life'),
                }
                try:
                    col_player.update_one({'UserName': username}, {'$set': new_info})
                    col_player.update_one({'UserName': username}, {'$pull': {'Equip': equip}})
                    col_player.update_one({'UserName': username}, {'$push': {'Package': equip}})

                except:
                    print('装备卸掉出现错误！')

                break

    return redirect('/display/pk')


@app_player.route('/displayer/pk', methods=['POST'])
def pk():
    data = request.form
    player_list = [data.get('player1'), data.get('player2')]
    random.shuffle(player_list)
    # print(player_list)
    p1=player_list[0]
    p2=player_list[1]


    p1_info=col_player.find_one({'UserName':p1})
    p2_info = col_player.find_one({'UserName': p2})

    p1_ATC=p1_info.get('ATC')
    p2_DEF=p2_info.get('DEF')
    if p1_ATC > p2_DEF:
        ATC=(p1_ATC-p2_DEF)*0.8
    else:
        ATC=(p1_ATC)*0.6
    p2_LIFE=p2_info.get('LIFE')-ATC
    if p2_LIFE <= 0:
        p2_LIFE=0
    col_player.update_one({'UserName':p2},{'$set':{'LIFE':p2_LIFE}})

    str=f'{p1}攻击{p2}-----{p2}生命值减少{ATC}，剩余{p2_LIFE}'
    t=time.strftime('%Y-%m-%d %X')
    col_record.insert_one({'time':t,'content':str})

    return jsonify({'url':'/display','time':t})








