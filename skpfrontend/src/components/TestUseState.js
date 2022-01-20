import React, {useState, useEffect} from "react";

const TestUseState =  () => {
    const [data, setData] = useState([]);

    const color = [
        {   
            id: 1,
            col: 'blue'
        },
        {
            id: 69,
            col: 'red'
        }
    ];
    
    useEffect(() => {setData(color)}, []);

    return(
        <div>
            <h1>These are the colors:</h1>
            {data.map(function(d, idx){
            return (<li key={idx}>{d.col}</li>)
            })}
        </div>
    )
}

export default TestUseState;