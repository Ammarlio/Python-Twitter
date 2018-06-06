import React from "react";
import $ from "jquery";

export default class App extends React.Component {

constructor(props) {
       super(props);
       this.state ={
       tweets:[]
       }

       this.getPythonHello = this.getPythonHello.bind(this);
   }

renderTweets(data){
    this.setState({tweet:data})
}

getPythonHello() {
       $.get(window.location.href + 'hello', (data) => {
           console.log(data);
           this.renderTweets(data)
       });
   }



 render () {
   return (
   <div style={{textAlign:'center'}}>
    <button type="button" onClick={this.getPythonHello}>Get 100 Tweets</button>
    <div>{this.state.tweet}</div>
    </div>

)}

}