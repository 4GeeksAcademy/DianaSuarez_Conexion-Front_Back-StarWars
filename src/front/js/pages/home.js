import React, { useContext, useEffect, useState } from "react";
import { Context } from "../store/appContext.js";
import "../../styles/home.css";
import { CardPeople } from "../component/cardpeople.js";
import { useNavigate } from "react-router-dom";

export const Home = () => {
	const { store, actions } = useContext(Context);
	const navigate = useNavigate();

	useEffect(() => {
		actions.getPeople()
	}, [])

	return (
		<div className="text-danger ms-5"><h1>People</h1>
		{/* <Signup/> */}
			<div className="Map Cards text-dark d-flex">
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

