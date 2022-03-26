def Create(SessionId):
    return {
        "platform": "seneca-web",
        "clientVersion": "2.4.128",
        "session": {
            "sessionId": SessionId,
            "sessionType": "adaptive",
            "courseId": "2670ac10-1d69-11e8-bf76-f14a3ef7c0e6",
            "sectionIds": ["eb52d2e0-1d6b-11e8-8e43-0b8b5e91224a"],
            "contentIds": [],
            "modulesStudied": 15,
            "modulesTested": 9,
            "modulesCorrect": 9,
            "modulesIncorrect": 0,
            "modulesGaveUp": 0,
            "averageScore": 1,
            "sessionScore": 1,
            "timeStarted": "2022-03-25T19:04:28+00:00",
            "timeFinished": "2022-03-25T23:17:17+00:00",
            "startingProficiency": 0.9662722814208937,
            "endingProficiency": 0.9766666666666667,
            "startingCourseProficiency": 0.012078403517761172,
            "endingCourseProficiency": 0.012208333333333333,
            "endingCourseScore": 0.008849557522123894,
            "completed": True,
            "smartLearningActive": False,
            "signedOut": False,
            "wrongModuleIds": [],
            "totalModulesStudyTime": 0
        },
        "modules": [
            {
                "sessionId": SessionId,
                "moduleOrder": 0,
                "courseId": "2670ac10-1d69-11e8-bf76-f14a3ef7c0e6",
                "sectionId": "eb52d2e0-1d6b-11e8-8e43-0b8b5e91224a",
                "contentId": "321858d0-1d6c-11e8-8e43-0b8b5e91224a",
                "moduleId": "321858d1-1d6c-11e8-8e43-0b8b5e91224a",
                "moduleType": "image-description",
                "testingActive": False,
                "content": {
                    "title": "Atomic Model",
                    "words": ["An atom has a small, positively-charged nucleus surrounded by orbiting negatively-charged electrons."],
                    "imageURL": "seneca-image-cdn:///courseImages/physics/5.1.1%20Atomic%20model/5.1.1-Atomic-model-adapted%20(2)-min.png",
                    "image": {
                        "url": "https://image-v2.cdn.app.senecalearning.com/courseImages/physics/5.1.1%20Atomic%20model/5.1.1-Atomic-model-adapted%20(2)-min,f_inside,h_300,w_550.png",
                        "fallbackUrl": None
                    },
                    "renderImage": True
                },
                "userAnswer": {},
                "score": None,
                "moduleScore": {},
                "timeStarted": "2022-03-25T19:04:30+00:00",
                "timeFinished": "2022-03-25T19:10:23+00:00",
                "gaveUp": False,
                "submitted": False,
                "completed": True
            },
            {
                "sessionId": SessionId,
                "moduleOrder": 1,
                "courseId": "2670ac10-1d69-11e8-bf76-f14a3ef7c0e6",
                "sectionId": "eb52d2e0-1d6b-11e8-8e43-0b8b5e91224a",
                "contentId": "321858d0-1d6c-11e8-8e43-0b8b5e91224a",
                "moduleId": "32187fe2-1d6c-11e8-8e43-0b8b5e91224a",
                "moduleType": "toggles",
                "testingActive": True,
                "content": {
                    "statement": "Which of the following statements are true of atoms?",
                    "toggles": [
                        {
                            "index1": "They have a positive nucleus",
                            "index0": "They have a negative nucleus",
                            "correctAnswer": 1
                        },
                        {
                            "index0": "Electrons orbit the nucleus",
                            "index1": "Protons orbit the nucleus",
                            "correctAnswer": 0
                        },
                        {
                            "index1": "They are very tiny - a few hundred picometres across",
                            "index0": "They are quite large - about a centimetre across",
                            "correctAnswer": 1
                        }
                    ],
                    "initialAnswer": [0, 0, 0]
                },
                "userAnswer": [1, 0, 1],
                "score": 1,
                "moduleScore": {"score": 1},
                "timeStarted": "2022-03-25T19:10:23+00:00",
                "timeFinished": "2022-03-25T19:10:30+00:00",
                "gaveUp": False,
                "submitted": True,
                "completed": True
            },
            {
                "sessionId": SessionId,
                "moduleOrder": 2,
                "courseId": "2670ac10-1d69-11e8-bf76-f14a3ef7c0e6",
                "sectionId": "eb52d2e0-1d6b-11e8-8e43-0b8b5e91224a",
                "contentId": "321858d0-1d6c-11e8-8e43-0b8b5e91224a",
                "moduleId": "32187fe3-1d6c-11e8-8e43-0b8b5e91224a",
                "moduleType": "delve",
                "testingActive": False,
                "content": {
                    "title": "Nucleus",
                    "description": "The nucleus contains [protons](Protons) and neutrons in the centre. [Electrons](Electrons) orbit outside of the nucleus.",
                    "children": [
                        {
                            "title": "Protons",
                            "description": "A small, positively charged particle found in the nucleus.",
                            "parent": "Nucleus"
                        },
                        {
                            "title": "Electrons",
                            "description": "An electron is a small, negatively charged particle that orbits the nucleus.",
                            "parent": "Nucleus"
                        }
                    ]
                },
                "userAnswer": {},
                "score": None,
                "moduleScore": {},
                "timeStarted": "2022-03-25T19:10:30+00:00",
                "timeFinished": "2022-03-25T19:10:31+00:00",
                "gaveUp": False,
                "submitted": False,
                "completed": True
            },
            {
                "sessionId": SessionId,
                "moduleOrder": 3,
                "courseId": "2670ac10-1d69-11e8-bf76-f14a3ef7c0e6",
                "sectionId": "eb52d2e0-1d6b-11e8-8e43-0b8b5e91224a",
                "contentId": "326feeb0-1d6c-11e8-8e43-0b8b5e91224a",
                "moduleId": "326feeb1-1d6c-11e8-8e43-0b8b5e91224a",
                "moduleType": "image-description",
                "testingActive": False,
                "content": {
                    "title": "Structure of an Atom",
                    "words": ["- Atoms are very small and have a radius of about 1 × 10<sup>-10 </sup> metres.\n- The electrons are arranged at different distances from the nucleus (different energy levels). \n- The radius of a nucleus is less than 1/10 000 of the radius of an atom. \n- Most of the mass of an atom is concentrated in the nucleus."],
                    "imageURL": "seneca-image-cdn:///courseImages/physics/AQA%20New%20Modules/6.1.1/structure%20atom.png",
                    "image": {
                        "url": "https://image-v2.cdn.app.senecalearning.com/courseImages/physics/AQA%20New%20Modules/6.1.1/structure%20atom,f_inside,h_300,w_550.png",
                        "fallbackUrl": None
                    },
                    "renderImage": True
                },
                "userAnswer": {},
                "score": None,
                "moduleScore": {},
                "timeStarted": "2022-03-25T19:10:31+00:00",
                "timeFinished": "2022-03-25T19:10:32+00:00",
                "gaveUp": False,
                "submitted": False,
                "completed": True
            },
            {
                "sessionId": SessionId,
                "moduleOrder": 4,
                "courseId": "2670ac10-1d69-11e8-bf76-f14a3ef7c0e6",
                "sectionId": "eb52d2e0-1d6b-11e8-8e43-0b8b5e91224a",
                "contentId": "326feeb0-1d6c-11e8-8e43-0b8b5e91224a",
                "moduleId": "326feeb2-1d6c-11e8-8e43-0b8b5e91224a",
                "moduleType": "concept",
                "testingActive": False,
                "content": {
                    "gifExamples": True,
                    "randomExampleOrder": False,
                    "title": "Size of Atoms vs Nucleus",
                    "explanation": "Atoms have a radius of radius of about 1 × 10<sup>-10 </sup> metres. However, the nucleus of atoms are even smaller. ",
                    "examples": [
                        {
                            "title": "Atoms",
                            "example": "- If an atom was the size of Wembley Stadium, then...",
                            "image": {
                                "url": "https://media.giphy.com/media/l49JNOhwsfiJmdZQs/giphy.mp4",
                                "fallbackUrl": "https://gif.app.senecalearning.com/media/l49JNOhwsfiJmdZQs/giphy.mp4"
                            }
                        },
                        {
                            "title": "Nucleus",
                            "example": "- ...its nucleus would be the size of a garden pea!",
                            "image": {
                                "url": "https://media.giphy.com/media/xTiTnekiQtHA5rcmis/giphy.mp4",
                                "fallbackUrl": "https://gif.app.senecalearning.com/media/xTiTnekiQtHA5rcmis/giphy.mp4"
                            }
                        }
                    ]
                },
                "userAnswer": {},
                "score": None,
                "moduleScore": {},
                "timeStarted": "2022-03-25T19:10:32+00:00",
                "timeFinished": "2022-03-25T19:10:33+00:00",
                "gaveUp": False,
                "submitted": False,
                "completed": True
            },
            {
                "sessionId": SessionId,
                "moduleOrder": 5,
                "courseId": "2670ac10-1d69-11e8-bf76-f14a3ef7c0e6",
                "sectionId": "eb52d2e0-1d6b-11e8-8e43-0b8b5e91224a",
                "contentId": "326feeb0-1d6c-11e8-8e43-0b8b5e91224a",
                "moduleId": "326feeb6-1d6c-11e8-8e43-0b8b5e91224a",
                "moduleType": "toggles",
                "testingActive": True,
                "content": {
                    "statement": "Which of the following has the largest mass?",
                    "toggles": [
                        {
                            "index1": "An atom",
                            "index0": "An atom's nucleus",
                            "correctAnswer": 1
                        },
                        {
                            "index1": "An atom's nucleus",
                            "index0": "An atom's energy levels",
                            "correctAnswer": 1
                        }
                    ],
                    "initialAnswer": [0, 1]
                },
                "userAnswer": [1, 1],
                "score": 1,
                "moduleScore": {"score": 1},
                "timeStarted": "2022-03-25T19:10:33+00:00",
                "timeFinished": "2022-03-25T19:10:35+00:00",
                "gaveUp": False,
                "submitted": True,
                "completed": True
            },
            {
                "sessionId": SessionId,
                "moduleOrder": 6,
                "courseId": "2670ac10-1d69-11e8-bf76-f14a3ef7c0e6",
                "sectionId": "eb52d2e0-1d6b-11e8-8e43-0b8b5e91224a",
                "contentId": "32ac5b70-1d6c-11e8-8e43-0b8b5e91224a",
                "moduleId": "32ac5b71-1d6c-11e8-8e43-0b8b5e91224a",
                "moduleType": "concept",
                "testingActive": False,
                "content": {
                    "randomExampleOrder": False,
                    "title": "The Charges of Sub-Atomic Particles",
                    "explanation": "The 3 different sub-atomic particles (protons, neutrons and electrons) have different relative charges. Atoms have no overall charge (are neutral). In an atom, these charges all cancel each other out. ",
                    "examples": [
                        {
                            "title": "Protons (+1)",
                            "example": "- Protons have a relative charge of +1.\n- They are found in the nucleus.\n- An element’s atomic number is the number of protons it possesses. \n - All atoms of the same element have the same number of protons.",
                            "image": {
                                "url": "https://image-v2.cdn.app.senecalearning.com/courseImages/chemistry/1.1.2%20-%20Model%20of%20the%20atom/1.1.3.1%20Atom,f_cover,h_400,w_600.jpg",
                                "fallbackUrl": None
                            }
                        },
                        {
                            "title": "Electrons (-1)",
                            "example": "- Electrons have a relative charge of -1.\n- They are found in fixed orbits around the nucleus.\n- In any atom, the total number of negative electrons equals the number of positive protons, meaning atoms have no overall electric charge.",
                            "image": {
                                "url": "https://image-v2.cdn.app.senecalearning.com/courseImages/chemistry/1.1.2%20-%20Model%20of%20the%20atom/1.1.3.1%20Atom,f_cover,h_400,w_600.jpg",
                                "fallbackUrl": None
                            }
                        },
                        {
                            "title": "Neutrons (0)",
                            "example": "- Neutrons have a relative charge of 0 - they are neutral.\n- Like protons, they are found in the nucleus.",
                            "image": {
                                "url": "https://image-v2.cdn.app.senecalearning.com/courseImages/chemistry/1.1.2%20-%20Model%20of%20the%20atom/1.1.3.1%20Atom,f_cover,h_400,w_600.jpg",
                                "fallbackUrl": None
                            }
                        }
                    ]
                },
                "userAnswer": {},
                "score": None,
                "moduleScore": {},
                "timeStarted": "2022-03-25T19:10:35+00:00",
                "timeFinished": "2022-03-25T19:10:36+00:00",
                "gaveUp": False,
                "submitted": False,
                "completed": True
            },
            {
                "sessionId": SessionId,
                "moduleOrder": 7,
                "courseId": "2670ac10-1d69-11e8-bf76-f14a3ef7c0e6",
                "sectionId": "eb52d2e0-1d6b-11e8-8e43-0b8b5e91224a",
                "contentId": "32ac5b70-1d6c-11e8-8e43-0b8b5e91224a",
                "moduleId": "32ac5b78-1d6c-11e8-8e43-0b8b5e91224a",
                "moduleType": "multiple-choice",
                "testingActive": True,
                "content": {
                    "question": "What is the overall charge of the nucleus of an atom?",
                    "answers": ["Negative", "Positive", "Neutral"],
                    "correctAnswerIndex": 1
                },
                "userAnswer": {"index": 1},
                "score": 1,
                "moduleScore": {"score": 1},
                "timeStarted": "2022-03-25T19:10:36+00:00",
                "timeFinished": "2022-03-25T19:10:39+00:00",
                "gaveUp": False,
                "submitted": True,
                "completed": True
            },
            {
                "sessionId": SessionId,
                "moduleOrder": 8,
                "courseId": "2670ac10-1d69-11e8-bf76-f14a3ef7c0e6",
                "sectionId": "eb52d2e0-1d6b-11e8-8e43-0b8b5e91224a",
                "contentId": "32ac5b70-1d6c-11e8-8e43-0b8b5e91224a",
                "moduleId": "32ac5b72-1d6c-11e8-8e43-0b8b5e91224a",
                "moduleType": "delve",
                "testingActive": False,
                "content": {
                    "title": "Atoms",
                    "description": "Atoms are made up of a [nucleus](Nucleus) and orbiting [electrons](Electrons).",
                    "children": [
                        {
                            "description": "A nucleus is at the centre of an atom. It contains [protons](Protons) and [neutrons](Neutrons). ",
                            "parent": "Atoms",
                            "title": "Nucleus",
                            "children": [
                                {
                                    "title": "Protons",
                                    "description": "The positive charge of protons cancels out the negative charge of the electrons. ",
                                    "parent": "Nucleus"
                                },
                                {
                                    "title": "Neutrons",
                                    "description": "Neutrons have the same mass as protons but have no charge. ",
                                    "parent": "Nucleus"
                                }
                            ]
                        },
                        {
                            "title": "Electrons",
                            "description": "Electrons are negatively charged particles that orbit the nucleus at fixed distances. ",
                            "parent": "Atoms"
                        }
                    ]
                },
                "userAnswer": {},
                "score": None,
                "moduleScore": {},
                "timeStarted": "2022-03-25T19:10:39+00:00",
                "timeFinished": "2022-03-25T19:10:40+00:00",
                "gaveUp": False,
                "submitted": False,
                "completed": True
            },
            {
                "sessionId": SessionId,
                "moduleOrder": 9,
                "courseId": "2670ac10-1d69-11e8-bf76-f14a3ef7c0e6",
                "sectionId": "eb52d2e0-1d6b-11e8-8e43-0b8b5e91224a",
                "contentId": "321858d0-1d6c-11e8-8e43-0b8b5e91224a",
                "moduleId": "32187fe1-1d6c-11e8-8e43-0b8b5e91224a",
                "moduleType": "wordfill",
                "testingActive": True,
                "content": {
                    "words": [
                        "An atom has a small, ",
                        {
                            "otherPermittedWords": ["positive", "+1"],
                            "word": "positively",
                            "testing": True
                        },
                        " charged nucleus surrounded by orbiting negatively charged ",
                        {
                            "otherPermittedWords": [],
                            "word": "electrons",
                            "testing": True
                        },
                        "."
                    ],
                    "imageURL": "https://image-v2.cdn.app.senecalearning.com/courseImages/physics/5.1.1.1%20-%20Model%20of%20atom-min,f_cover,h_250,w_1024.png",
                    "renderImage": False
                },
                "userAnswer": {"words": {
                        "positively": "positively",
                        "electrons": "electrons"
                    }},
                "score": 1,
                "moduleScore": {
                    "words": {
                        "positively": True,
                        "electrons": True
                    },
                    "score": 1
                },
                "timeStarted": "2022-03-25T19:10:40+00:00",
                "timeFinished": "2022-03-25T19:10:43+00:00",
                "gaveUp": False,
                "submitted": True,
                "completed": True
            },
            {
                "sessionId": SessionId,
                "moduleOrder": 10,
                "courseId": "2670ac10-1d69-11e8-bf76-f14a3ef7c0e6",
                "sectionId": "eb52d2e0-1d6b-11e8-8e43-0b8b5e91224a",
                "contentId": "326feeb0-1d6c-11e8-8e43-0b8b5e91224a",
                "moduleId": "326feeb3-1d6c-11e8-8e43-0b8b5e91224a",
                "moduleType": "multiple-choice",
                "testingActive": True,
                "content": {
                    "question": "In what environment would the relative mass of an atom change?",
                    "answers": ["On the Moon", "Mass is constant across all environments", "In deep space"],
                    "correctAnswerIndex": 1,
                    "image": {
                        "url": "https://image-v2.cdn.app.senecalearning.com/courseImages/physics/AQA%20New%20Modules/6.1.1/structure%20atom,f_inside,h_267,w_400.png",
                        "fallbackUrl": None
                    }
                },
                "userAnswer": {"index": 1},
                "score": 1,
                "moduleScore": {"score": 1},
                "timeStarted": "2022-03-25T19:10:43+00:00",
                "timeFinished": "2022-03-25T19:10:49+00:00",
                "gaveUp": False,
                "submitted": True,
                "completed": True
            },
            {
                "sessionId": SessionId,
                "moduleOrder": 11,
                "courseId": "2670ac10-1d69-11e8-bf76-f14a3ef7c0e6",
                "sectionId": "eb52d2e0-1d6b-11e8-8e43-0b8b5e91224a",
                "contentId": "32ac5b70-1d6c-11e8-8e43-0b8b5e91224a",
                "moduleId": "32ac5b77-1d6c-11e8-8e43-0b8b5e91224a",
                "moduleType": "grid",
                "testingActive": True,
                "content": {
                    "title": "Relative charge of sub-atomic particles",
                    "definitions": [
                        {
                            "word": "Neutron",
                            "text": "0",
                            "testing": True
                        },
                        {
                            "word": "Electron",
                            "text": "-1",
                            "testing": True
                        },
                        {
                            "word": "Proton",
                            "text": "+1",
                            "testing": True
                        }
                    ]
                },
                "userAnswer": {"definitions": {
                        "Neutron": "Neutron",
                        "Electron": "Electron",
                        "Proton": "Proton"
                    }},
                "score": 1,
                "moduleScore": {
                    "definitions": {
                        "Neutron": True,
                        "Electron": True,
                        "Proton": True
                    },
                    "score": 1
                },
                "timeStarted": "2022-03-25T19:10:49+00:00",
                "timeFinished": "2022-03-25T19:10:51+00:00",
                "gaveUp": False,
                "submitted": True,
                "completed": True
            },
            {
                "sessionId": SessionId,
                "moduleOrder": 12,
                "courseId": "2670ac10-1d69-11e8-bf76-f14a3ef7c0e6",
                "sectionId": "eb52d2e0-1d6b-11e8-8e43-0b8b5e91224a",
                "contentId": "321858d0-1d6c-11e8-8e43-0b8b5e91224a",
                "moduleId": "32187fe8-1d6c-11e8-8e43-0b8b5e91224a",
                "moduleType": "multiple-choice",
                "testingActive": True,
                "content": {
                    "question": "What do we call a small, negatively charged particle that orbits an atom's nucleus?",
                    "answers": ["Proton", "Element", "Ion", "Electron", "Compound"],
                    "correctAnswerIndex": 3
                },
                "userAnswer": {"index": 3},
                "score": 1,
                "moduleScore": {"score": 1},
                "timeStarted": "2022-03-25T19:10:51+00:00",
                "timeFinished": "2022-03-25T19:10:56+00:00",
                "gaveUp": False,
                "submitted": True,
                "completed": True
            },
            {
                "sessionId": SessionId,
                "moduleOrder": 13,
                "courseId": "2670ac10-1d69-11e8-bf76-f14a3ef7c0e6",
                "sectionId": "eb52d2e0-1d6b-11e8-8e43-0b8b5e91224a",
                "contentId": "326feeb0-1d6c-11e8-8e43-0b8b5e91224a",
                "moduleId": "326feeb7-1d6c-11e8-8e43-0b8b5e91224a",
                "moduleType": "wordfill",
                "testingActive": True,
                "content": {
                    "words": [
                        "An atom's ",
                        {
                            "otherPermittedWords": [],
                            "word": "electrons",
                            "testing": True
                        },
                        " are arranged at different distances from the nucleus (different energy levels). ."
                    ],
                    "fact": True,
                    "renderImage": False
                },
                "userAnswer": {"words": {"electrons": "electrons"}},
                "score": 1,
                "moduleScore": {
                    "words": {"electrons": True},
                    "score": 1
                },
                "timeStarted": "2022-03-25T19:10:56+00:00",
                "timeFinished": "2022-03-25T19:11:04+00:00",
                "gaveUp": False,
                "submitted": True,
                "completed": True
            },
            {
                "sessionId": SessionId,
                "moduleOrder": 14,
                "courseId": "2670ac10-1d69-11e8-bf76-f14a3ef7c0e6",
                "sectionId": "eb52d2e0-1d6b-11e8-8e43-0b8b5e91224a",
                "contentId": "32ac5b70-1d6c-11e8-8e43-0b8b5e91224a",
                "moduleId": "32ac5b73-1d6c-11e8-8e43-0b8b5e91224a",
                "moduleType": "list",
                "testingActive": True,
                "content": {
                    "pretest": "SOMETIMES",
                    "multipleChoice": {
                        "question": "How many types of sub-atomic particles are there in an atom?",
                        "answers": ["5", "2", "4", "3"],
                        "correctAnswerIndex": 3
                    },
                    "list": {
                        "statement": "Sub-atomic particles",
                        "values": [
                            {
                                "value": [
                                    {
                                        "otherPermittedWords": [],
                                        "word": "proton",
                                        "caps": "Proton"
                                    }
                                ],
                                "testing": True
                            },
                            {
                                "value": [
                                    {
                                        "otherPermittedWords": [],
                                        "word": "neutron",
                                        "caps": "Neutron"
                                    }
                                ],
                                "testing": True
                            },
                            {
                                "value": [
                                    {
                                        "otherPermittedWords": [],
                                        "word": "electron",
                                        "caps": "Electron"
                                    }
                                ],
                                "testing": True
                            }
                        ]
                    }
                },
                "userAnswer": {
                    "multipleChoice": {"index": 3},
                    "list": ["Proton", "Electron", "Neutron"]
                },
                "score": 1,
                "moduleScore": {
                    "score": 1,
                    "multipleChoice": {"score": 1},
                    "list": {
                        "score": 1,
                        "hits": [True, True, True]
                    }
                },
                "timeStarted": "2022-03-25T19:11:04+00:00",
                "timeFinished": "2022-03-25T19:11:17+00:00",
                "gaveUp": False,
                "submitted": True,
                "completed": True
            }
        ]
    }