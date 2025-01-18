# Meet&Mingle. API

This is the testing document for the backend of my MeetandMingle project. If you want to see the README, click [here](README.md).

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

### Followers app

| File            | Status |
|-----------------|--------|
| models.py       | ✅     |
| serializers.py  | ✅     |
| urls.py         | ✅     |
| views.py        | ✅     |

### Likes app

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

### Category app

| File            | Status |
|-----------------|--------|
| models.py       | ✅     |
| serializers.py  | ✅     |
| urls.py         | ✅     |
| views.py        | ✅     |


### Event app

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

Can list Profiles | ✅
Can retrieve profile using valid ID | ✅
Can update own profile | ✅
Can't update someone else's profile | ✅
Can't delete someone else's profile | ✅

Can list followers | ✅
Logged in user can follow | ✅
Logged out user can't follow | ✅
Can retrieve followers using valid ID | ✅
Can delete follow from my own profile | ✅
Can't retrieve followers using invalid ID | ✅

Can list likes | ✅
Logged in user can like | ✅
Can delete own likes | ✅
Can retrieve likes using valid ID | ✅
Logged out user can't like | ✅
Can't delete someone else's likes | ✅
Can't like the same post twice | ✅

Can list posts | ✅
Can update own post | ✅
Logged out user can't create post | ✅
Logged in user can create post | ✅
Can't delete someone else's post | ✅
Can't update someone else's post | ✅
Can't retrieve post using invalid ID | ✅
Can't retrieve profile using invalid ID | ✅

Can list comments | ✅
Logged in user can create comment | ✅
Can't retrieve comment using invalid ID | ✅
Can retrieve comment using valid ID | ✅
Can't update someone else's comment | ✅
Can't delete someone else's comments | ✅
Can update own comment | ✅
Can delete own comment | ✅

Can list categories | ✅
Can choose categories for the own posts | ✅
Can add or delete new categories | ✅
Can add images to categories | ✅


Can retrieve event using valid ID | ✅
Can list events | ✅
Logged in user can create event | ✅
Logged out user can't create event | ✅
Can update own events | ✅
Can delete own events | ✅
Can't update/delete someone else's events | ✅



[Back to top](<#content>)