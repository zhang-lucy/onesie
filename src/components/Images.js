import React, { Component } from 'react';


class Images extends Component {
    constructor(props) {
      super(props);
      this.state = { listOfImages: [] };
    }
    importAll(r) {
      return r.keys().map(r);
    }
  
    render() {
      return (
        <>
        {img}
          <ul>
            <li>
              {this.state.listOfImages.map((image, index) => (
                <img src={image} key={index} alt="info"></img>
              ))}
            </li>
          </ul>
        </>
      );
    }
  }
  
  export default Images;