import pymongo
mycli = pymongo.MongoClient('127.0.0.1', 27017)
mydb = mycli['play']
col_player=mydb['players']
col_record=mydb['pkRec']
players_list = [
    {
        'UserName': 'Player1',
        'ATC': 15,
        'DEF': 40,
        'LIFE': 500,
        'Equip': [],
        'Package': [
            {'name': '黄金甲', 'atc': -5, 'def': 20, 'life': 200},
            {'name': '98K', 'atc': 20, 'def': -5, 'life': 0},
            {'name': '饮料', 'atc': 5, 'def': 0, 'life': 100},
        ]
    },
    {
        'UserName': 'Player2',
        'ATC': 20,
        'DEF': 30,
        'LIFE': 450,
        'Equip': [],
        'Package': [
            {'name': '二级甲', 'atc': -5, 'def': 20, 'life': 200},
            {'name': 'AK47', 'atc': 20, 'def': -5, 'life': 0},
            {'name': '急救包', 'atc': 0, 'def': 0, 'life': 300},
        ]
    },
]

# col_player.insert_many(players_list)
# col_player.update_one({'UserName':'Player1'},{'$set':{'UserName': 'Player1',
#         'ATC': 15,
#         'DEF': 40,
#         'LIFE': 500,
#         'Equip': [],
#         'Package': [
#             {'name': '黄金甲', 'atc': -5, 'def': 20, 'life': 200},
#             {'name': '98K', 'atc': 20, 'def': -5, 'life': 0},
#             {'name': '饮料', 'atc': 5, 'def': 0, 'life': 100},
#         ]}})


# col_player.update_one({'UserName':'Player2'},{'$set':{'UserName': 'Player2',
#         'ATC': 20,
#         'DEF': 30,
#         'LIFE': 450,
#         'Equip': [],
#         'Package': [
#             {'name': '二级甲', 'atc': -5, 'def': 20, 'life': 200},
#             {'name': 'AK47', 'atc': 20, 'def': -5, 'life': 0},
#             {'name': '急救包', 'atc': 0, 'def': 0, 'life': 300},
#         ]}})



# for player in col_player.find({}):
#     print('----------------------------------------------------------------------')
#     for key,val in player.items():
#         print(f'{key}:{val}')
# print('----------------------------------------------------------------------')
# for i in col_record.find({}):
#     print(i)

