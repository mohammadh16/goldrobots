							const currentTime = new Date();
                                            const startTime = new Date();
                                            startTime.setHours(12);
                                            startTime.setMinutes(0);
                                            startTime.setSeconds(1);
                                            const endTime = new Date();
                                            endTime.setHours(9);
                                            endTime.setMinutes(0);
                                            endTime.setSeconds(0);
                                            if (currentTime >= startTime && currentTime <= endTime) {
                                                console.log("test");
                                                var america = document.getElementsByName("america");
                                                for (var i = 0, max = america.length; i < max; i++) {
                                                    america[i].style.fill = "#BA6D18";
                                                }
                                            }