#!/usr/bin/env bash

#запуск тестов в консоли

#запуск vk_chat_bot
psql -U postgres -d vk_chat_bot

coverage run --source=bot, settings, handlers -m unittest
coverage report -m

#create Postgres database
psql -U postgres -c "create database vk_chat_bot"
#кодировка
psql -U postgres -d vk_chat_bot
psql \! chcp 1251

#удаление таблицы
drop table userstate;

#содержимое таблицы
select * from userstate;