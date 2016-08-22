ATTACKER = '''{
    "package": {
        "killID": 55680988,
        "killmail": {
            "solarSystem": {
                "id_str": "30002970",
                "href": "https://crest-tq.eveonline.com/solarsystems/30002970/",
                "id": 30002970,
                "name": "Ohide"
            },
            "killID": 55680988,
            "killTime": "2016.08.21 16:18:40",
            "attackers": [
                {
                    "shipType": {
                        "id_str": "3885",
                        "href": "https://crest-tq.eveonline.com/inventory/types/3885/",
                        "id": 3885,
                        "name": "CONCORD Police Captain",
                        "icon": {
                            "href": "http://imageserver.eveonline.com/Type/3885_128.png"
                        }
                    },
                    "corporation": {
                        "id_str": "1000125",
                        "href": "https://crest-tq.eveonline.com/corporations/1000125/",
                        "id": 98319972,
                        "name": "CONCORD",
                        "icon": {
                            "href": "http://imageserver.eveonline.com/Corporation/1000125_128.png"
                        }
                    },
                    "damageDone_str": "689",
                    "finalBlow": true,
                    "securityStatus": 0,
                    "damageDone": 689
                }
            ],
            "attackerCount": 1,
            "victim": {
                "damageTaken": 689,
                "items": [
                    {
                        "singleton": 0,
                        "itemType": {
                            "id_str": "34",
                            "href": "https://crest-tq.eveonline.com/inventory/types/34/",
                            "id": 34,
                            "name": "Tritanium",
                            "icon": {
                                "href": "http://imageserver.eveonline.com/Type/34_128.png"
                            }
                        },
                        "quantityDestroyed_str": "1",
                        "flag": 5,
                        "flag_str": "5",
                        "singleton_str": "0",
                        "quantityDestroyed": 1
                    },
                    {
                        "singleton": 0,
                        "itemType": {
                            "id_str": "3638",
                            "href": "https://crest-tq.eveonline.com/inventory/types/3638/",
                            "id": 3638,
                            "name": "Civilian Gatling Railgun",
                            "icon": {
                                "href": "http://imageserver.eveonline.com/Type/3638_128.png"
                            }
                        },
                        "quantityDestroyed_str": "1",
                        "flag": 27,
                        "flag_str": "27",
                        "singleton_str": "0",
                        "quantityDestroyed": 1
                    },
                    {
                        "singleton": 0,
                        "itemType": {
                            "id_str": "3651",
                            "href": "https://crest-tq.eveonline.com/inventory/types/3651/",
                            "id": 3651,
                            "name": "Civilian Miner",
                            "icon": {
                                "href": "http://imageserver.eveonline.com/Type/3651_128.png"
                            }
                        },
                        "quantityDestroyed_str": "1",
                        "flag": 28,
                        "flag_str": "28",
                        "singleton_str": "0",
                        "quantityDestroyed": 1
                    }
                ],
                "damageTaken_str": "689",
                "character": {
                    "id_str": "91719989",
                    "href": "https://crest-tq.eveonline.com/characters/91719989/",
                    "id": 91719989,
                    "name": "Alan Hekki",
                    "icon": {
                        "href": "http://imageserver.eveonline.com/Character/91719989_128.jpg"
                    }
                },
                "shipType": {
                    "id_str": "601",
                    "href": "https://crest-tq.eveonline.com/inventory/types/601/",
                    "id": 601,
                    "name": "Ibis",
                    "icon": {
                        "href": "http://imageserver.eveonline.com/Type/601_128.png"
                    }
                },
                "corporation": {
                    "id_str": "98243573",
                    "href": "https://crest-tq.eveonline.com/corporations/98243573/",
                    "id": 98243573,
                    "name": "Space Slowpokes",
                    "icon": {
                        "href": "http://imageserver.eveonline.com/Corporation/98243573_128.png"
                    }
                },
                "position": {
                    "y": 167311314869.91,
                    "x": 1413511814243.8,
                    "z": 697601922983.87
                }
            },
            "killID_str": "55680988",
            "attackerCount_str": "1",
            "war": {
                "href": "https://crest-tq.eveonline.com/wars/0/",
                "id": 0,
                "id_str": "0"
            }
        },
        "zkb": {
            "locationID": 60001180,
            "hash": "cff419ca58ff9f43eb50eff96b237fc85a8e13bf",
            "totalValue": 10220.12,
            "points": 18,
            "href": "https://crest-tq.eveonline.com/killmails/55680988/cff419ca58ff9f43eb50eff96b237fc85a8e13bf/"
        }
    }
}'''

ATTACKER_SLACK = '''{
    "attachments": [
        {
            "title": "CONCORD Police Captain (CONCORD) killed Alan Hekki (Space Slowpokes)",
            "color": "good",
            "thumb_url": "https://imageserver.eveonline.com/Render/601_64.png",
            "fields": [
                {
                    "title": "Damage taken",
                    "short": true,
                    "value": "689"
                },
                {
                    "title": "Pilots involved",
                    "short": true,
                    "value": 1
                },
                {
                    "title": "Value",
                    "short": true,
                    "value": "10,220.12 ISK"
                },
                {
                    "title": "Ship",
                    "short": true,
                    "value": "Ibis"
                },
                {
                    "title": "Location",
                    "short": true,
                    "value": "<https://zkillboard.com/system/30002970/|Ohide>"
                }
            ],
            "fallback": "CONCORD Police Captain (CONCORD) killed Alan Hekki (Space Slowpokes)",
            "title_link": "https://zkillboard.com/kill/55680988/"
        }
    ]
}'''

VICTIM = '''{
    "package": {
        "killID": 55680988,
        "killmail": {
            "solarSystem": {
                "id_str": "30002970",
                "href": "https://crest-tq.eveonline.com/solarsystems/30002970/",
                "id": 30002970,
                "name": "Ohide"
            },
            "killID": 55680988,
            "killTime": "2016.08.21 16:18:40",
            "attackers": [
                {
                    "shipType": {
                        "id_str": "3885",
                        "href": "https://crest-tq.eveonline.com/inventory/types/3885/",
                        "id": 3885,
                        "name": "CONCORD Police Captain",
                        "icon": {
                            "href": "http://imageserver.eveonline.com/Type/3885_128.png"
                        }
                    },
                    "corporation": {
                        "id_str": "1000125",
                        "href": "https://crest-tq.eveonline.com/corporations/1000125/",
                        "id": 1000125,
                        "name": "CONCORD",
                        "icon": {
                            "href": "http://imageserver.eveonline.com/Corporation/1000125_128.png"
                        }
                    },
                    "damageDone_str": "689",
                    "finalBlow": true,
                    "securityStatus": 0,
                    "damageDone": 689
                }
            ],
            "attackerCount": 1,
            "victim": {
                "damageTaken": 689,
                "items": [
                    {
                        "singleton": 0,
                        "itemType": {
                            "id_str": "34",
                            "href": "https://crest-tq.eveonline.com/inventory/types/34/",
                            "id": 34,
                            "name": "Tritanium",
                            "icon": {
                                "href": "http://imageserver.eveonline.com/Type/34_128.png"
                            }
                        },
                        "quantityDestroyed_str": "1",
                        "flag": 5,
                        "flag_str": "5",
                        "singleton_str": "0",
                        "quantityDestroyed": 1
                    },
                    {
                        "singleton": 0,
                        "itemType": {
                            "id_str": "3638",
                            "href": "https://crest-tq.eveonline.com/inventory/types/3638/",
                            "id": 3638,
                            "name": "Civilian Gatling Railgun",
                            "icon": {
                                "href": "http://imageserver.eveonline.com/Type/3638_128.png"
                            }
                        },
                        "quantityDestroyed_str": "1",
                        "flag": 27,
                        "flag_str": "27",
                        "singleton_str": "0",
                        "quantityDestroyed": 1
                    },
                    {
                        "singleton": 0,
                        "itemType": {
                            "id_str": "3651",
                            "href": "https://crest-tq.eveonline.com/inventory/types/3651/",
                            "id": 3651,
                            "name": "Civilian Miner",
                            "icon": {
                                "href": "http://imageserver.eveonline.com/Type/3651_128.png"
                            }
                        },
                        "quantityDestroyed_str": "1",
                        "flag": 28,
                        "flag_str": "28",
                        "singleton_str": "0",
                        "quantityDestroyed": 1
                    }
                ],
                "damageTaken_str": "689",
                "character": {
                    "id_str": "91719989",
                    "href": "https://crest-tq.eveonline.com/characters/91719989/",
                    "id": 91719989,
                    "name": "Alan Hekki",
                    "icon": {
                        "href": "http://imageserver.eveonline.com/Character/91719989_128.jpg"
                    }
                },
                "shipType": {
                    "id_str": "601",
                    "href": "https://crest-tq.eveonline.com/inventory/types/601/",
                    "id": 601,
                    "name": "Ibis",
                    "icon": {
                        "href": "http://imageserver.eveonline.com/Type/601_128.png"
                    }
                },
                "corporation": {
                    "id_str": "98243573",
                    "href": "https://crest-tq.eveonline.com/corporations/98243573/",
                    "id": 98319972,
                    "name": "Space Slowpokes",
                    "icon": {
                        "href": "http://imageserver.eveonline.com/Corporation/98243573_128.png"
                    }
                },
                "position": {
                    "y": 167311314869.91,
                    "x": 1413511814243.8,
                    "z": 697601922983.87
                }
            },
            "killID_str": "55680988",
            "attackerCount_str": "1",
            "war": {
                "href": "https://crest-tq.eveonline.com/wars/0/",
                "id": 0,
                "id_str": "0"
            }
        },
        "zkb": {
            "locationID": 60001180,
            "hash": "cff419ca58ff9f43eb50eff96b237fc85a8e13bf",
            "totalValue": 10220.12,
            "points": 18,
            "href": "https://crest-tq.eveonline.com/killmails/55680988/cff419ca58ff9f43eb50eff96b237fc85a8e13bf/"
        }
    }
}'''

VICTIM_SLACK = '''{
    "attachments": [
        {
            "title": "CONCORD Police Captain (CONCORD) killed Alan Hekki (Space Slowpokes)",
            "color": "danger",
            "thumb_url": "https://imageserver.eveonline.com/Render/601_64.png",
            "fields": [
                {
                    "title": "Damage taken",
                    "short": true,
                    "value": "689"
                },
                {
                    "title": "Pilots involved",
                    "short": true,
                    "value": 1
                },
                {
                    "title": "Value",
                    "short": true,
                    "value": "10,220.12 ISK"
                },
                {
                    "title": "Ship",
                    "short": true,
                    "value": "Ibis"
                },
                {
                    "title": "Location",
                    "short": true,
                    "value": "<https://zkillboard.com/system/30002970/|Ohide>"
                }
            ],
            "fallback": "CONCORD Police Captain (CONCORD) killed Alan Hekki (Space Slowpokes)",
            "title_link": "https://zkillboard.com/kill/55680988/"
        }
    ]
}'''
