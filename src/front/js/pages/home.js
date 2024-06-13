import React, { useContext, useEffect, useState } from "react";
import { Context } from "../store/appContext.js";
import "../../styles/home.css";
import { CardPeople } from "../component/cardpeople.js";
import { Signup } from "../component/signup.js";
import Login from "../component/login.js";

export const Home = () => {
	const { store, actions } = useContext(Context);

	useEffect(() => {
		actions.getPeople()
	}, [])

	return (
		<div className="text-danger ms-5"><h1>Characters</h1>
		{/* <Signup/> */}
			<div className="Map Cards text-dark d-flex" style={{ overflowX: "scroll" }}>
				{store.peoples.map((card) => {
					//   console.log(card);
					return (
						<CardPeople card={card} key={card.uid} />
					)
				})
				}
			</div>
		</div>
	)
};

