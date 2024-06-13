import React, { Component, useState, useContext } from "react";
import { Context } from "../store/appContext";
import { Link } from "react-router-dom";

export const Signup = () => {

    const [name, setName] = useState("")
    const [email, setEmail] = useState("")
    const [password, setPassword] = useState("")
    const { store, actions } = useContext(Context);
    // console.log(actions.login);

    function handlesubmit(e) {
        e.preventDefault();
        // console.log(name, email, password);
        // actions.login()
        actions.signup(name, email, password)
    }

    return (
        <form onSubmit={handlesubmit} className="w-50 mx-auto">
            <div className="mb-3"></div>
            <div className="mb-3">
                <label htmlFor="exampleInputName1" className="form-label">Name</label>
                <input value={name} type="text" className="form-control" onChange={(e) => setName(e.target.value)} id="exampleInputEmail1" aria-describedby="emailHelp" />
            </div>
            <div className="mb-3">
                <label htmlFor="exampleInputEmail1" className="form-label">Email address</label>
                <input value={email} type="email" className="form-control" onChange={(e) => setEmail(e.target.value)} id="exampleInputEmail1" aria-describedby="emailHelp" />
            </div>
            <div className="mb-3">
                <label htmlFor="exampleInputPassword1" className="form-label">Password</label>
                <input value={password} type="password" className="form-control" onChange={(e) => setPassword(e.target.value)} id="exampleInputPassword1" />
            </div>
            <div className="mb-3 form-check">
                <input type="checkbox" className="form-check-input" id="exampleCheck1" />
                <label className="form-check-label" htmlFor="exampleCheck1">Check me out</label>
            </div>
            {/* <button type="submit" className="btn btn-primary">Submit</button>
            <Link to={'/login'}>
                <button type="submit" className="btn btn-primary">Login</button>
            </Link> */}
        </form>
    )
};