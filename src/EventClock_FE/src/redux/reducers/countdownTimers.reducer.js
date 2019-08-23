const defaultCounntdowns = [
    {
        id: 'Auditorium',
        ip: '192.168.12.143',
        time: 0,
    },
    {
        id: 'BlackSea',
        ip: '192.168.12.143',
        time: 0
    },
    {
        id: 'Marathon',
        ip: '192.168.12.143',
        time: 0
    },
    {
        id: 'Tours',
        ip: '192.168.12.143',
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