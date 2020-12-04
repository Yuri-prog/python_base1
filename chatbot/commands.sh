#!/usr/bin/env bash

#запуск тестов в консоли
python -m unittest
#запуск vk_chat_bot
psql -U postgres -d vk_chat_bot

coverage run --source=bot, settings, handlers -m unittest
coverage report -m

#create Postgres database
psql -U postgres -c "create database vk_chat_bot"
psql -U postgres -d vk_chat_bot