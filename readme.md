# 🧵 Yarn Count Calculator

A simple educational web application for calculating yarn count from given length and weight parameters.

Designed for **2nd Year Textile Engineering students**.

## Features

The application calculates yarn count using four common yarn count systems:

1. English Cotton Count (Ne)
2. Metric Count (Nm)
3. Tex
4. Denier

Students select the count system, enter the length and weight, and the application calculates the yarn count.

---

## Yarn Count Systems

### 1. English Cotton Count (Ne)

English Cotton Count is an indirect yarn numbering system.

Formula:

Ne = Length (yards) / [840 × Weight (lb)]

A higher Ne indicates a finer yarn.

---

### 2. Metric Count (Nm)

Metric Count is an indirect yarn numbering system.

Formula:

Nm = Length (meters) / Weight (kg)

A higher Nm indicates a finer yarn.

---

### 3. Tex

Tex is a direct yarn numbering system.

Formula:

Tex = Weight (grams) / Length (km)

A higher Tex indicates a coarser/heavier yarn.

---

### 4. Denier

Denier is a direct yarn numbering system.

Formula:

Denier = Weight (grams) × 9000 / Length (meters)

A higher Denier indicates a coarser/heavier yarn.

---

## Project Structure

```text
yarn-count-calculator/
│
├── app.py
├── requirements.txt
└── README.md
