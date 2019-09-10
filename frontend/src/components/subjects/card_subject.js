import React from 'react'

const CardSubject = ({ name, image }) => {

  return(
    <div className="card">
      <div className="card-image">
        <figure className="image is-4by3">
          <img src={image} alt="Algebra book page"/>
        </figure>
        <hr/>
      </div>
      <div className="card-content">
        <div className="content has-text-centered title is-4">{name}</div>
      </div>
    </div>
  )
}

export default CardSubject
