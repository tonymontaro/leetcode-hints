package leetcode

import (
	"fmt"
	"net/http"
	"net/url"
)

func AccountsLogin(username, password string) (*http.Response, error) {
	resp, err := http.Head(accountsLoginUrl)
	checkErr(err)
	defer resp.Body.Close()
	saveCookies(resp.Cookies())
	csrftoken := getCsrfToken(resp.Cookies())
	data := url.Values{
		"login":               {username},
		"password":            {password},
		"csrfmiddlewaretoken": {csrftoken},
	}
	resp, err = http.PostForm(accountsLoginUrl, data)
	checkErr(err)
	defer resp.Body.Close()
	saveCookies(resp.Cookies())
	if resp.StatusCode == 200 {
		saveCredential(data)
	} else {
		fmt.Println("login error: ", resp.Status)
	}
	return resp, err
}

func AutoLogin() (*http.Response, error) {
	data := getCredential()
	if data.Get("login") == "" {
		fmt.Println("can't get username")
	}
	if data.Get("password") == "" {
		fmt.Println("can't get password")
	}
	return AccountsLogin(data.Get("login"), data.Get("password"))
}
