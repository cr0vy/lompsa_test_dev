#!/usr/bin/env python3

from fastapi import FastAPI

app = FastAPI()

incomes = [
    {
        "year": 2020,
        "month": "January"
    },
    {
        "year": 2020,
        "month": "February"
    },
    {
        "year": 2020,
        "month": "March"
    },
    {
        "year": 2020,
        "month": "April"
    },
    {
        "year": 2020,
        "month": "May"
    }
]

expenses = [
    {
        "year": 2020,
        "month": "January"
    },
    {
        "year": 2020,
        "month": "February"
    },
    {
        "year": 2020,
        "month": "March"
    },
    {
        "year": 2020,
        "month": "April"
    },
    {
        "year": 2020,
        "month": "May"
    }
]


@app.get("/")
async def get_all():
    return incomes, expenses


@app.get("/month/{month_id}")
async def get_monthly(month_id: int):
    m_id = month_id - 1
    return incomes[m_id], expenses[m_id]


@app.get("/expenses")
async def get_expenses():
    return expenses


@app.get("/expenses/{month_id}")
async def get_monthly_expense(month_id: int):
    return expenses[month_id - 1]


@app.get("/incomes", status_code=200)
async def get_incomes():
    return incomes


@app.get("/incomes/{month_id}")
async def get_monthly_income(month_id: int):
    return incomes[month_id - 1]
