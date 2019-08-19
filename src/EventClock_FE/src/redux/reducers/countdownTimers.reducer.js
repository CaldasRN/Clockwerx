const defaultCounntdowns = [
    {
        id: 'Auditorium',
        time: 0
    },
    {
        id: 'BlackSea',
        time: 0
    },
    {
        id: 'Marathon',
        time: 0
    },
    {
        id: 'Tours',
        time: 0
    }
];

// const action = {
//      type: 'ADD_TIMER',
//      payload: {
//         id: 'room03',
//         time: 0
//      }
// }
const countdownTimers = (state = defaultCounntdowns, action) => {
    switch (action.type) {
        case 'ADD_TIMER':
            return [ ...state, action.payload ];
        default:
            return state;
    }
};

export default countdownTimers;