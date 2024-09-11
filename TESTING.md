# MeetandMingle. API

This is the testing document for the backend of my connectify. project. If you want to see the README, click [here](README.md).

# Testing

## Content

* [Testing](<#testing>)
    * [Code Validation](<#code-validation>)
    * [Manual Testing](<#manual-testing>)

## Code Validation 

The code has been validated by the [Code Institute's PEP8 validator](https://pep8ci.herokuapp.com/).

### drf_api

| File            | Status |
|-----------------|--------|
| permissions.py  | ✅     |
| serializers.py  | ✅     |
| views.py        | ✅     |
| models.py       | ✅     |
| urls.py         | ✅     |


### Followers app

| File            | Status |
|-----------------|--------|
| models.py       | ✅     |
| serializers.py  | ✅     |
| urls.py         | ✅     |
| views.py        | ✅     |


### Comments app

| File            | Status |
|-----------------|--------|
| models.py       | ✅     |
| serializers.py  | ✅     |
| urls.py         | ✅     |
| views.py        | ✅     |

### Posts app

| File            | Status |
|-----------------|--------|
| models.py       | ✅     |
| serializers.py  | ✅     |
| urls.py         | ✅     |
| views.py        | ✅     |

### Favorites app

| File            | Status |
|-----------------|--------|
| models.py       | ✅     |
| serializers.py  | ✅     |
| urls.py         | ✅     |
| views.py        | ✅     |

### Followers app

| File            | Status |
|-----------------|--------|
| models.py       | ✅     |
| serializers.py  | ✅     |
| urls.py         | ✅     |
| views.py        | ✅     |

### Profiles app

| File            | Status |
|-----------------|--------|
| models.py       | ✅     |
| serializers.py  | ✅     |
| urls.py         | ✅     |
| views.py        | ✅     |

### Messaging app

| File            | Status |
|-----------------|--------|
| models.py       | ✅     |
| serializers.py  | ✅     |
| urls.py         | ✅     |
| views.py        | ✅     |

[Back to top](<#content>)

## Manual Testing

Some manual tests have been carried out.

| Test            | Status |
|-----------------|--------|
Can retrieve followers using valid ID | ✅
Can list posts | ✅
Can delete follow from my own profile | ✅
Logged out user can't create event/post | ✅
Can't write a message | ✅
Can update own post/event | ✅
Can update own profile | ✅
Can't update someone else's profile | ✅
Can list comments | ✅
Logged in user can favorite | ✅
Can retrieve favorites using valid ID | ✅
Can't retrieve post using invalid ID | ✅
Can delete own favorites | ✅
Can't retrieve comment using invalid ID | ✅
Can retrieve comment using valid ID | ✅
Can list followers | ✅
Can't delete someone else's favorites | ✅
Can't favorite the same event twice | ✅
Can't retrieve profile using invalid ID | ✅
Can't update someone else's comment | ✅
Can retrieve event using valid ID | ✅
Can't delete someone else's post | ✅
Can update own comment | ✅
Can't retrieve followers using invalid ID | ✅
Can't delete someone else's message | ✅
Can delete own comment | ✅
Logged in user can create post | ✅
Can retrieve profile using valid ID | ✅
Can list favorites | ✅
Logged out user can't favorite | ✅
Can't delete someone else's profile | ✅
Logged out user can't follow | ✅
Can list profiles | ✅
Logged in user can follow | ✅
Logged in user can create comment | ✅
Can't delete someone else's comment | ✅
Can't update someone else's post | ✅
Can list posts | ✅

[Back to top](<#content>)