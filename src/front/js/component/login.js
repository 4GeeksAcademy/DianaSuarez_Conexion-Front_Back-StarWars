import React, { Component, useState, useContext } from "react";
import { Context } from "../store/appContext";
import { Link, useNavigate } from "react-router-dom";

export const Login = () => {

    const navigate= useNavigate()
    const [email, setEmail] = useState("")
    const [password, setPassword] = useState("")
    const { store, actions } = useContext(Context);

    function handlesubmit(e) {
        e.preventDefault();
        actions.login(email, password, navigate)
    }

    return (
        <form onSubmit={handlesubmit} className="w-50 mx-auto">
            <div className="mb-3"></div>
            <div className="mb-3">
                <label for="exampleInputEmail1" className="form-label">Email address</label>
                <input value={email} type="email" className="form-control" onChange={(e) => setEmail(e.target.value)} id="exampleInputEmail1" aria-describedby="emailHelp" />
                <div id="emailHelp" className="form-text">We'll never share your email with anyone else.</div>
            </div>
            <div className="mb-3">
                <label for="exampleInputPassword1" className="form-label">Password</label>
                <input value={password} type="password" className="form-control" onChange={(e) => setPassword(e.target.value)} id="exampleInputPassword1" />
            </div>
            <div className="mb-3 form-check">
                <input type="checkbox" className="form-check-input" id="exampleCheck1" />
                <label className="form-check-label" for="exampleCheck1">Check me out</label>
            </div>
            <button type="submit" className="btn btn-primary">Submit</button>
            <Link to={'/signup'}>
                <button type="submit" className="btn btn-primary">Register</button>
            </Link>
        </form>
    )
}